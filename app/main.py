from app.models import ChatRequest, ChatResponse

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    reply = route_intent(req.message)
    return {"response": reply}

#Run using
#uvicorn app.main:app --reload
