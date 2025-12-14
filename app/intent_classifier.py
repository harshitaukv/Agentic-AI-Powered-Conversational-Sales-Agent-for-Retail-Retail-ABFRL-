from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from app.llm import get_llm

llm = get_llm()

prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Classify the user intent into ONE of the following:
- recommendation
- inventory
- payment
- post_purchase
- general

User input: {text}
Intent:
"""
)

intent_chain = LLMChain(llm=llm, prompt=prompt)

def detect_intent(user_input: str) -> str:
    intent = intent_chain.run(text=user_input)
    return intent.strip().lower()
