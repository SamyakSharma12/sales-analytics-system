def read_sales_data(filepath):
    records = []
    with open(filepath, "r", encoding="latin1") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            fields = line.split("|")
            records.append(fields)
    return records
