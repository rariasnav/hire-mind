import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def load_openai_api_key():
    """Load OpenAI API key from environment variables."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("❌ no OPENAI_API_KEY found in environment.")
    return api_key


def create_vector_store(docs: list[str]) -> FAISS:
    """Create a FAISS vector store from the provided documents using OpenAI embeddings."""

    if not docs:
        st.warning("❌ No documents provided for vector store creation.")    
        return None

    api_key = load_openai_api_key()

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        openai_api_key=api_key
    )
    
    vectorstore = FAISS.from_texts(docs, embedding=embeddings)
    return vectorstore