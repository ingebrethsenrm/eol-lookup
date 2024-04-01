# Author: Rudi Mitander Ingebrethsen
# Date: 2024-03-31

"""
This script looks up End-of-Life dates for products. Search string is the product ID.
The initial purpose is to look up network equipment, such as AP's, switches, routers, etc. 
"""

import csv
import datetime
import argparse
import os
import sys

csv_data_file = "eol-list.csv"

def get_eol_date(product_id, data_file=csv_data_file):
    """
    Finds the End-of-Life date for a given product ID.

    Args:
        product_id (str): The product ID to search for.
        data_file (str): Path to the CSV file containing EOL data.

    Returns:
        str: Found EOL date in ISO 8601 format (YYYYMMDD), or None if not found
    """

    script_dir = os.path.dirname(__file__) # Get the directory of the script
    data_file_path = os.path.join(script_dir, data_file) # Construct the full path

    with open(data_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == product_id:
                return row[1]  # Return YYYYMMDD format
    return None

# Argument parsing
parser = argparse.ArgumentParser(description="Lookup EOL dates.")

# Add usage examples after the other arguments
parser.add_argument("product_id", help="Product ID to search for")
parser.add_argument("-f", "--format", default="%Y%m%d", 
                    help="Output date format (e.g., %%Y%%m%%d (dafault), %%d.%%m.%%Y)")
parser.add_argument("-i", "--include-id", action="store_true",
                    help="Include product ID in output")

# Add examples as a formatted string
examples = f"Usage Examples:\n  1. {os.path.basename(sys.argv[0])} abc1234 (Default date format YYYYMMDD ISO 8601)\n  2. {os.path.basename(sys.argv[0])} xyz9876 -f %d.%m.%Y -i (Custom date format and include product ID)"
parser.formatter_class = argparse.RawDescriptionHelpFormatter  # Preserve formatting
parser.epilog = examples

args = parser.parse_args()

# Get and format EOL date
eol_date_iso = get_eol_date(args.product_id)

if eol_date_iso:
    try:
        output_date = datetime.datetime.strptime(eol_date_iso, "%Y%m%d").strftime(args.format)
        if args.include_id:
            print(f"{args.product_id}: {output_date}")
        else:
            print(output_date)
    except ValueError:
        print(f"Invalid date format in CSV for product ID: {args.product_id}")
else:
    print(f"Product ID not found: {args.product_id}") 
