import os
import csv

# Construct the paths
home_dir = os.path.expanduser('~')
input_csv_file_path = os.path.join(home_dir, 'Downloads', 'filtered_products.csv')
output_csv_file_path = os.path.join(home_dir, 'Downloads', 'filtered_brands.csv')

# List of brand owners to filter on
brand_owners = [
    "The Kroger Co.",
    "HY-VEE",
    "HY-VEE FISH MARKET",
    "KROGER",
    "PUBLIX",
    "TRADER JOE'S",
    "AHOLD",
    "Whole Foods Market, Inc.",
    "Wal-Mart Stores, Inc.",
    "WHOLE FOODS MARKET",
    "TRADER JACQUES",
    "WHOLE FOODS MARKETS",
    "TRADER GIOTTO'S",
    "TRADER MING'S",
    "TRADER JOSE'S",
    "Ahold Usa, Inc.",
    "Giant Eagle, Inc.",
    "Hy-Vee, Inc.",
    "WAL-MART",
    "GIANT EAGLE MARKET DISTRICT",
    "Publix Super Markets, Inc.",
    "DOLLAR GENERAL CORPORATION",
    "PUBLIX BAKERY",
    "Aldi Inc.",
    "Ahold USA, Inc.",
    "Family Dollar Stores Inc.",
    "Costco Companies Inc.",
    "Dollar Tree Stores, Inc.",
    "Walgreens Co.",
    "CVS Pharmacy, Inc.",
    "Piggly Wiggly Company",
    "ALDI",
    "365 WHOLE FOODS MARKET",
    "Wal-Mart United States",
    "The Kroger Company",
    "365 by Whole Foods Market Services",
    "WHOLE FOODS MARKET - PGC",
    "Piggly Wiggly North Carolina, LLC",
    "Kroger Corporate Brands",
    "WALMART",
    "Albertsons Companies"
]

# Convert brand owners to a set for faster lookup and normalize case
brand_owners_set = set(brand_owners)

# Open the input and output CSV files
with open(input_csv_file_path, 'r', encoding='utf-8') as input_file, \
     open(output_csv_file_path, 'w', newline='', encoding='utf-8') as output_file:

    reader = csv.DictReader(input_file)
    writer = None

    count_total = 0
    count_filtered = 0

    for row in reader:
        count_total += 1
        brand_owner = row.get('brandOwner', '').strip()

        if brand_owner in brand_owners_set:
            count_filtered += 1
            if writer is None:
                # Initialize the CSV writer with fieldnames from the input file
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(output_file, fieldnames=fieldnames)
                writer.writeheader()
            writer.writerow(row)

    print(f"Total items processed: {count_total}")
    print(f"Total items written to CSV: {count_filtered}")
