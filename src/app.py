import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
from src.generator import answer_query

st.set_page_config(page_title="RAG Terminal", page_icon="🖥️", layout="centered")


st.markdown("""
<style>
    .stApp {
        background-color: #0a0a0f;
        color: #ffb000;
        font-family: 'Courier New', monospace;
    }
    h1, h2, h3, p, label, .stMarkdown {
        color: #ffb000 !important;
        text-shadow: 0 0 6px #66ff;
    }
    .stTextInput > div > div > input {
        background-color: #0a0a0f;
        color: #66ff00;
        border: 1px solid #00c8d2;
        font-family: 'Courier New', monospace;
    }
    .stButton > button {
        background-color: #0a0a0f;
        color: #00c8d2;
        border: 1px solid #00c8d2;
        font-family: 'Courier New', monospace;
    }
    .stButton > button:hover {
        background-color: #ff3c78;
        color: #0a0a0f;
    }
</style>
""", unsafe_allow_html=True)

st.title("▚ RAG TERMINAL ▞")
st.caption("offline knowledge assistant · foundry local · no internet")

question = st.text_input("QUERY >", placeholder="ask your documents...")

if st.button("TRANSMIT") and question:
    with st.spinner("retrieving + generating..."):
        answer = answer_query(question)
    st.markdown("**RESPONSE:**")
    st.markdown(answer)