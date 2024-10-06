# Food Data Filter Script

This script processes a large JSON file containing food data, filters out items based on specified unwanted oils in the ingredients, and exports the filtered data to a CSV file.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
  - [Adjusting Unwanted Oils](#adjusting-unwanted-oils)
  - [Changing File Paths](#changing-file-paths)
  - [Modifying Progress Logging](#modifying-progress-logging)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

P.S. - HERE IS THE LINK TO THE USDA SITE https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_branded_food_json_2024-04-18.zip
---

## Overview

The script efficiently handles large JSON datasets by using incremental parsing with the `ijson` library. It filters out food items that contain specific unwanted oils in their ingredients list and writes the filtered data to a CSV file. The script also handles nested JSON structures and data types like `Decimal` to ensure the CSV output is correctly formatted.

## Features

- **Incremental JSON Parsing**: Efficiently parses large JSON files without loading the entire file into memory.
- **Customizable Filtering**: Easily adjust the list of unwanted oils to filter out specific ingredients.
- **Data Serialization**: Handles nested data structures and serializes them appropriately for CSV output.
- **Progress Logging**: Provides updates on the processing progress for large datasets.
- **Error Handling**: Manages data types that are not JSON serializable by default, such as `Decimal`.

## Prerequisites

- **Python 3.6** or higher
- **Libraries**:
  - `ijson`
  - `csv`
  - `re`
  - `json`
  - `decimal` (standard library)

## Installation

1. **Clone the Repository** (if applicable):

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Required Libraries**:

   ```bash
   pip install ijson
   ```

   The other libraries used (`csv`, `re`, `json`, `decimal`, and `os`) are part of the Python Standard Library and do not require installation.

## Usage

1. **Place the JSON File**:

   - Ensure that your JSON file is named `brandedDownload.json`.
   - Place it in the `Downloads` directory of your home folder.

2. **Run the Script**:

   ```bash
   python filter_foods.py
   ```

3. **Output**:

   - The filtered data will be written to `filtered_products.csv` in your `Downloads` directory.
   - The script will print progress updates every 10,000 items processed.

## Customization

### Adjusting Unwanted Oils

To change the list of oils you want to filter out, modify the `contains_unwanted_oils` function:

```python
def contains_unwanted_oils(ingredients):
    pattern = r'\b(GRAPESEED OIL|SUNFLOWER OIL|SOYBEAN OIL|COTTONSEED OIL|CORN OIL)\b'
    return re.search(pattern, ingredients, re.IGNORECASE)
```

- **Add Oils**: Include additional oils by adding them to the pattern, separated by `|`.
- **Example**:

  ```python
  pattern = r'\b(GRAPESEED OIL|SUNFLOWER OIL|SOYBEAN OIL|COTTONSEED OIL|CORN OIL|CANOLA OIL|PALM OIL)\b'
  ```

### Changing File Paths

To change the input or output file locations, modify the file path variables:

```python
home_dir = os.path.expanduser('~')
json_file_path = os.path.join(home_dir, 'Downloads', 'brandedDownload.json')
csv_file_path = os.path.join(home_dir, 'Downloads', 'filtered_products.csv')
```

- **Custom Input File**:

  ```python
  json_file_path = '/path/to/your/input_file.json'
  ```

- **Custom Output File**:

  ```python
  csv_file_path = '/path/to/your/output_file.csv'
  ```

### Modifying Progress Logging

Adjust how frequently the script reports its progress by changing the `count_total` modulo value:

```python
if count_total % 10000 == 0:
    print(f"Processed {count_total} items...")
```

- **More Frequent Updates**: Use a smaller number.
- **Less Frequent Updates**: Use a larger number.

## Troubleshooting

- **CSV File Not Opening**:

  - **Issue**: The CSV file is too large for applications like Excel.
  - **Solution**: Use a text editor capable of handling large files (e.g., VSCode, Sublime Text) or a dedicated CSV viewer.

- **Encoding Issues**:

  - **Issue**: Special characters are not displayed correctly.
  - **Solution**: Ensure the application opening the CSV file supports UTF-8 encoding.

- **Permission Errors**:

  - **Issue**: Script cannot read or write files due to permission restrictions.
  - **Solution**: Check the file paths and ensure you have the necessary permissions.

- **Decimal Serialization Error**:

  - **Issue**: `TypeError: Object of type Decimal is not JSON serializable`.
  - **Solution**: The script includes a custom `decimal_default` function to handle `Decimal` objects. Ensure this function is present and correctly implemented.

- **CSV Formatting Issues**:

  - **Issue**: The CSV file appears broken or improperly formatted.
  - **Solution**: The script processes nested data structures and converts them to JSON strings. Ensure that `process_item` function is correctly implemented to handle all data types.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**:

   Click the "Fork" button at the top right of the repository page.

2. **Clone Your Fork**:

   ```bash
   git clone https://github.com/yourusername/your-fork.git
   cd your-fork
   ```

3. **Create a Feature Branch**:

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Commit Your Changes**:

   ```bash
   git commit -am 'Add your feature'
   ```

5. **Push to Your Fork**:

   ```bash
   git push origin feature/your-feature-name
   ```

6. **Submit a Pull Request**:

   Go to the original repository and create a pull request from your fork.

## License

This project is licensed under the [MIT License](LICENSE).

---

## Code Explanation

Below is a brief explanation of the main components of the script:

### Imports

```python
import os
import ijson
import csv
import re
import json
from decimal import Decimal
```

- **os**: Interacts with the operating system for file path operations.
- **ijson**: Parses JSON incrementally to handle large files efficiently.
- **csv**: Writes the filtered data to a CSV file.
- **re**: Provides regular expression matching operations.
- **json**: Handles JSON serialization of nested data structures.
- **decimal**: Manages `Decimal` data types that are not JSON serializable by default.

### File Paths

```python
home_dir = os.path.expanduser('~')
json_file_path = os.path.join(home_dir, 'Downloads', 'brandedDownload.json')
csv_file_path = os.path.join(home_dir, 'Downloads', 'filtered_products.csv')
```

- Constructs file paths for the input JSON and output CSV files.

### Filtering Function

```python
def contains_unwanted_oils(ingredients):
    pattern = r'\b(GRAPESEED OIL|SUNFLOWER OIL|SOYBEAN OIL|COTTONSEED OIL|CORN OIL)\b'
    return re.search(pattern, ingredients, re.IGNORECASE)
```

- Uses a regular expression to search for unwanted oils in the ingredients list.

### Decimal Serialization Handler

```python
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')
```

- Converts `Decimal` objects to `float` for JSON serialization.

### Item Processing Function

```python
def process_item(item):
    processed_item = {}
    for key, value in item.items():
        if isinstance(value, (list, dict)):
            processed_item[key] = json.dumps(value, default=decimal_default)
        elif isinstance(value, Decimal):
            processed_item[key] = float(value)
        else:
            processed_item[key] = value
    return processed_item
```

- Iterates over each item and ensures all values are serializable.
- Converts nested lists and dictionaries to JSON strings.
- Handles `Decimal` objects.

### Main Processing Loop

```python
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
            processed_item = process_item(item)
            writer.writerow(processed_item)

        if count_total % 10000 == 0:
            print(f"Processed {count_total} items...")

    print(f"Total items processed: {count_total}")
    print(f"Total items written to CSV: {count_filtered}")
```

- **File Handling**: Opens the JSON and CSV files.
- **Data Processing**: Iterates over each item, filters, and processes it.
- **CSV Writing**: Writes the processed items to the CSV file.
- **Progress Logging**: Prints updates every 10,000 items.
- **Summary**: Prints the total number of items processed and written.

---

Feel free to reach out if you have any questions or need further assistance!
