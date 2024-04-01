# EOL Lookup Script
A customizable Python script that looks up product End-of-Life (EOL) dates from a CSV file.
Supports case-insensitive product ID search and flexible output date formatting.

## Features
* Case-insensitive product ID search
* Customizable date output formatting

## Usage

1. **Prerequisites**
    * Python 3 (https://www.python.org/downloads/)

2. **Setup**
    * Download or clone this repository.
    * Use the included CSV file, or create your own. Populate it with product IDs and EOL dates int the format:
        ```
        product_id,YYYYMMDD
        ```

3. ***Run the script***
    * Ececute from the command line:
        ```bash
        python eol-lookup.py <product_id> [-f <output_format>] [-i]
        ```
    
    * **Arguments:**
        * `<product_id>`: The product ID to search for (required).
        * `-f <output_format>`:  Optional format for the output date.  Refer to Python's datetime formatting codes (e.g., %Y%m%d, %d.%m.%Y).  Defaults to %Y%m%d. 
        * `-i`:  Optional flag to include the product ID in the output. 

## Examples

```bash
python eol-lookup.py abc1234
# Output: abc1234: 20200530
```
```bash
python eol-lookup.py abc1234 -f %d-%m-%Y -i 
# Output: abc1234: 30-05-2020
```