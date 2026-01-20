import re

def clean_data(records):
    header = records[0]
    valid_records = []
    invalid_count = 0

    for row in records[1:]:
        if len(row) != len(header):
            invalid_count += 1
            continue

        record = dict(zip(header, row))

        if not record["CustomerID"] or not record["Region"]:
            invalid_count += 1
            continue

        if not record["TransactionID"].startswith("T"):
            invalid_count += 1
            continue

        try:
            quantity = int(record["Quantity"])
            price = float(record["UnitPrice"].replace(",", ""))
        except:
            invalid_count += 1
            continue

        if quantity <= 0 or price <= 0:
            invalid_count += 1
            continue

        record["ProductName"] = record["ProductName"].replace(",", "")
        record["Quantity"] = quantity
        record["UnitPrice"] = price

        valid_records.append(record)

    print(f"Total records parsed: {len(records) - 1}")
    print(f"Invalid records removed: {invalid_count}")
    print(f"Valid records after cleaning: {len(valid_records)}")

    return valid_records


def analyze_data(records):
    from collections import defaultdict

    summary = defaultdict(lambda: {"total_sales": 0, "total_quantity": 0})

    for r in records:
        key = r["ProductName"]
        summary[key]["total_sales"] += r["Quantity"] * r["UnitPrice"]
        summary[key]["total_quantity"] += r["Quantity"]

    return summary


def generate_report(analysis, output_path):
    with open(output_path, "w") as f:
        f.write("Product Report\n")
        f.write("================\n")
        for product, stats in analysis.items():
            f.write(f"{product}: Quantity Sold = {stats['total_quantity']}, Total Sales = ₹{stats['total_sales']:.2f}\n")
