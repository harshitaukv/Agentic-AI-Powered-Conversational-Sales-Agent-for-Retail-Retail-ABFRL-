from app.models import ChatRequest, ChatResponse
from app.analytics import get_analytics
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    reply = route_intent(req.message)
    return {"response": reply}
@app.get("/analytics")
def analytics():
    return get_analytics()

#Run using
#uvicorn app.main:app --reload
