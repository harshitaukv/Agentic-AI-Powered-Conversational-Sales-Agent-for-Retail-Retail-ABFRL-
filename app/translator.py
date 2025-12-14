from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo")

def translate(text: str, lang: str):
    if lang == "en":
        return text

    prompt = f"Translate this to {lang}: {text}"
    return llm.predict(prompt)

