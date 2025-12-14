from app.data import PRODUCTS

def search_products(query: str):
    results = []
    for p in PRODUCTS:
        if query.lower() in p["name"].lower() or query.lower() in p["category"].lower():
            results.append(p)
    return results

