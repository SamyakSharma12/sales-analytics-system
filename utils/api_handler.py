import requests

def fetch_product_info(records):
    # Dummy enrichment for demonstration
    for r in records:
        r["Category"] = "Electronics"
        r["StockStatus"] = "Available"
    return records
