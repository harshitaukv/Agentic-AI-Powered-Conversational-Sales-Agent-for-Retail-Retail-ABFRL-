from app.orchestrator import route_intent
def test_full_flow():
    inputs = [
        "Suggest a shirt",
        "Is it in stock?",
        "Proceed to payment",
        "Track my order"
    ]
    for i in inputs:
        print("User:", i)
        print("Bot:", route_intent(i))
        print("-" * 40)

