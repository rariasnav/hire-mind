import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

def create_vector_store(docs: list[str]):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.warning("❌ no OPENAI_API_KEY found in environment.")
        return None

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        openai_api_key=api_key
    )
    
    vectorstore = FAISS.from_texts(docs, embedding=embeddings)
    return vectorstore