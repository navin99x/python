import csv

header = ["name", "age", "major"]
record = ["aakash", 19, "bit"]

with open("demo.csv", mode='w', encoding='utf8', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(header)   # write header
    writer.writerow(record)   # write single row


# Writing multiple rows using DictWriter

data = [
    {"name": "aakash", "age": 23, "course": "csit"},
    {"name": "saksham", "age": 34, "course": "bca"}
]

with open("demo.csv", mode='a', newline='', encoding='utf8') as fp:
    fieldnames = ["name", "age", "major"]
    writer = csv.DictWriter(fp, fieldnames=fieldnames)

    writer.writerows(data)    # multiple rows


# Working with custom dialect

fieldnames = ["name", "age", "major"]

data = [
    {"name": "hari", "age": 20, "major": "bit"},
    {"name": "prakash", "age": 40, "major": "dbms"},
    {"name": "rabin", "age": 42, "major": "pie"}
]

# Register a dialect (custom delimiter, quoting, etc.)
csv.register_dialect(
    "custom",
    skipinitialspace=False,
    delimiter='|',
    quoting=csv.QUOTE_NONNUMERIC,   # quote only non-numeric fields
    quotechar="*"
)

with open("trial.csv", mode='a', encoding="utf-8", newline="") as fp:
    writer = csv.DictWriter(fp, fieldnames=fieldnames, dialect="custom")
    writer.writeheader()
    writer.writerows(data)