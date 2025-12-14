from app.intent_classifier import detect_intent
from app.agents.recommendation import recommend
from app.agents.inventory import inventory
from app.agents.payment import payment
from app.agents.post_purchase import post_purchase
from app.analytics import log_event

def route_intent(user_input: str):
    intent = detect_intent(user_input)
    log_event("intent_detected", intent)

    if intent == "recommendation":
        return recommend()
    if intent == "inventory":
        return inventory()
    if intent == "payment":
        return payment()
    if intent == "post_purchase":
        return post_purchase()
    if intent == "loyalty":
    return loyalty_offers()
    return "How can I help you today? 😊"
    from app.translator import translate
    response = process_logic(user_input)
    return translate(response, lang)

