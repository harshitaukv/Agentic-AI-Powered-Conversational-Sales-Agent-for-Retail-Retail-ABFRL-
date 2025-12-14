import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000/analytics"

st.set_page_config(page_title="ABFRL AI Dashboard", layout="wide")

st.title("📊 ABFRL Agentic AI – Live Analytics Dashboard")

data = requests.get(API_URL).json()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Recommendations", data["recommendations"])
col2.metric("Payments", data["payments"])
col3.metric("Returns", data["returns"])
col4.metric("Support Requests", data["support_requests"])

st.divider()

df = pd.DataFrame.from_dict(data, orient="index", columns=["Count"])
st.bar_chart(df)

st.divider()

st.subheader("📈 Agent Activity Distribution")
st.pie_chart(df)

