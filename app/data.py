
# Mock Product Catalog (ABFRL)
PRODUCTS = [
    {
        "id": "P1001",
        "name": "Slim Fit Cotton T-Shirt",
        "brand": "Allen Solly",
        "category": "Tops",
        "price": 1299
    },
    {
        "id": "P1002",
        "name": "Regular Fit Jeans",
        "brand": "Peter England",
        "category": "Bottoms",
        "price": 2499
    }
]

# -------------------------------
# Inventory Data
# -------------------------------
INVENTORY = {
    "P1001": {
        "status": "In Stock",
        "sizes": ["M", "L", "XL"],
        "quantity": 120
    },
    "P1002": {
        "status": "Limited Stock",
        "sizes": ["32", "34"],
        "quantity": 15
    }
}

# -------------------------------
# Customer Profile (Mock)
# -------------------------------
CUSTOMER_PROFILE = {
    "customer_id": "CUST101",
    "name": "Harshita",
    "preferred_brands": ["Allen Solly", "Van Heusen"],
    "purchase_history": ["P1001"]
}

# -------------------------------
# Orders
# -------------------------------
ORDERS = {
    "ABFRL-ORD-1029": {
        "product_id": "P1001",
        "status": "Out for Delivery",
        "delivery_date": "2025-01-20",
        "payment_status": "Paid"
    }
}

