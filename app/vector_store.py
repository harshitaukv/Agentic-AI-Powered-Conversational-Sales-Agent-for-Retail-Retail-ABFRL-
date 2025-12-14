from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from app.data import PRODUCTS

embeddings = OpenAIEmbeddings()

def build_vector_store():
    texts = [
        f"{p['brand']} {p['name']} {p['category']} price {p['price']}"
        for p in PRODUCTS
    ]
    return FAISS.from_texts(texts, embeddings)

vector_db = build_vector_store()

def search_products(query: str):
    docs = vector_db.similarity_search(query, k=2)
    return [d.page_content for d in docs]
