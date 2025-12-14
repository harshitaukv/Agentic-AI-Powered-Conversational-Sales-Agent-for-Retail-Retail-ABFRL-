from fastapi import FastAPI
from app.orchestrator import route_intent

app = FastAPI(title="ABFRL Agentic AI Sales Agent")

@app.post("/chat")
def chat(message: str):
    response = route_intent(message)
    return {"response": response}
#Run using
#uvicorn app.main:app --reload
