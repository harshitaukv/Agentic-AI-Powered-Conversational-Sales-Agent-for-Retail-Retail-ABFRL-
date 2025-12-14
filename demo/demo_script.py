from app.orchestrator import route_intent

queries = [
    "Recommend a shirt",
    "Is it available?",
    "Proceed to payment",
    "Track my order"
]

for q in queries:
    print("User:", q)
    print("Agent:", route_intent(q))
    print("-" * 50)

