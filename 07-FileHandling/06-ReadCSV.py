import csv

"""
CSV Handling in Python 
----------------------------------
1. csv.reader → Returns an iterator of rows (each row is a list)
2. csv.DictReader → Returns an iterator of rows as dictionaries
"""

file_path = "demo.txt"

try:
    with open(file_path, "r", newline='') as fp:
        csv_reader = csv.reader(fp)
        headers = next(csv_reader)
        print("Headers:", headers)

        # Iterate first 10 rows 
        for i, row in enumerate(csv_reader):
            if i >= 10:
                break
            print(f"Row {i + 1}:", row)

except FileNotFoundError:
    print(f"File {file_path} not found!")
except csv.Error as e:
    print("CSV parsing error:", e)
except Exception as error:
    print("Unexpected exception:", error)

# Using csv.DictReader

with open(file_path, "r", newline='') as f:
    csv_dict = csv.DictReader(f)

    # Example: Find a row where 'name' == "Nepal" and print its 'area'
    for record in csv_dict:
        if record.get('name') == "Nepal":
            print("Area of Nepal:", record.get("area"))
            break

