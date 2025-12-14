from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from app.llm import get_llm
from app.memory import memory

from app.agents.recommendation import recommend
from app.agents.inventory import inventory
from app.agents.payment import payment
from app.agents.post_purchase import post_purchase

llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an AI Sales Agent for ABFRL retail. "
     "Understand intent and route to the correct agent."),
    ("human", "{input}")
])

chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

def route_intent(user_input: str):
    text = user_input.lower()

    if "recommend" in text or "suggest" in text:
        return recommend()
    if "stock" in text or "available" in text:
        return inventory()
    if "pay" in text or "checkout" in text:
        return payment()
    if "track" in text or "return" in text:
        return post_purchase()

    return chain.run(input=user_input)

