from fastapi import FastAPI, Request
from twilio.twiml.messaging_response import MessagingResponse
from app.orchestrator import route_intent

app = FastAPI()

@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    incoming_msg = form.get("Body")

    reply = route_intent(incoming_msg)

    resp = MessagingResponse()
    resp.message(reply)
    return str(resp)

