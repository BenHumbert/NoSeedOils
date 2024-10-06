import os
import ijson
import csv
import re
import json  # Use simplejson if you choose Option 2
from decimal import Decimal

# Construct the paths
home_dir = os.path.expanduser('~')
json_file_path = os.path.join(home_dir, 'Downloads', 'brandedDownload.json')
csv_file_path = os.path.join(home_dir, 'Downloads', 'filtered_products.csv')

# Function to check for unwanted oils
def contains_unwanted_oils(ingredients):
    pattern = r'\b(GRAPESEED OIL|SUNFLOWER OIL|SOYBEAN OIL|COTTONSEED OIL|CORN OIL|CANOLA OIL|ORCANOLA OIL|CANOLA AND/OR SUNFLOWER OIL|NON-GMO EXPELLER PRESSED CANOLA OIL|NON-HYDROGENATED CANOLA OIL|ORGANIC EXPELLER PRESSED SOYBEAN OIL|SOYBEAN OILS|CANOLA OILS|VEGATABLE OIL|VEGATABLE OILS|FRACTIONATED PALM KERNEL OIL|FRACTIONATED PALM KERNEL OILS|HYDROGENATED PALM KERNEL OIL|PALM KERNEL OILS|PALM KERNEL OIL|HYDROGENATED|COTTONSEED OILS|COTTONSEED|CORN SYRUP|PALM OIL|VEGETABLE OIL|VEGETABLE OILS|FD & C RED#40)\b'
    return re.search(pattern, ingredients, re.IGNORECASE)

# Custom function to handle Decimal serialization
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)  # or return str(obj) for more precision
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

# Function to process each item
def process_item(item):
    processed_item = {}
    for key, value in item.items():
        if isinstance(value, (list, dict)):
            # Convert lists and dicts to JSON strings, handling Decimals
            processed_item[key] = json.dumps(value, default=decimal_default)
        elif isinstance(value, Decimal):
            # Convert Decimal to float or str
            processed_item[key] = float(value)  # or str(value)
        else:
            processed_item[key] = value
    return processed_item

# Open files
with open(json_file_path, 'r', encoding='utf-8') as json_file, \
     open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:

    writer = None
    items = ijson.items(json_file, 'BrandedFoods.item')
    count_total = 0
    count_filtered = 0

    for item in items:
        count_total += 1

        ingredients = item.get('ingredients', '')
        if not isinstance(ingredients, str) or not ingredients.strip():
            continue

        if not contains_unwanted_oils(ingredients):
            count_filtered += 1
            if writer is None:
                headers = item.keys()
                writer = csv.DictWriter(csv_file, fieldnames=headers, extrasaction='ignore')
                writer.writeheader()
            # Process the item before writing
            processed_item = process_item(item)
            writer.writerow(processed_item)

        # Progress logging
        if count_total % 10000 == 0:
            print(f"Processed {count_total} items...")

    print(f"Total items processed: {count_total}")
    print(f"Total items written to CSV: {count_filtered}")
