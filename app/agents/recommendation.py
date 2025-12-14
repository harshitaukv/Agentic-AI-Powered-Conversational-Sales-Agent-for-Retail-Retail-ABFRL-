from app.rag import search_products

def recommend():
    products = search_products("shirt")

    if not products:
        return "No matching products found."

    p = products[0]
    return (
        f"👕 *Recommended Product*\n"
        f"{p['brand']} {p['name']}\n"
        f"Category: {p['category']}\n"
        f"Price: ₹{p['price']}"
    )
