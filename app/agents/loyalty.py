from app.data import CUSTOMER_PROFILE

def loyalty_offers():
    points = 1200
    tier = "Gold"

    return (
        f"🎁 *Loyalty Summary*\n"
        f"Customer: {CUSTOMER_PROFILE['name']}\n"
        f"Tier: {tier}\n"
        f"Points: {points}\n"
        f"Offer: Flat ₹300 off on next purchase!"
    )

