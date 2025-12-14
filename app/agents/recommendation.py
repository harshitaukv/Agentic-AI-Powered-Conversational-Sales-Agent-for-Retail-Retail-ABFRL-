from app.vector_store import search_products

def recommend():
    results = search_products("cotton t-shirt")

    return (
        "👕 *AI Recommended Product*\n"
        + results[0]
        + "\nReason: Matches your preferences and current trends."
    )
