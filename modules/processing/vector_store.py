from langchain_community.vectorstores import FAISS
from pathlib import Path
import streamlit as st

def save_vector_store(vectorstore, path: str = "career_agent_index") -> None:
    """
    Save the vector store to a file.
    Create a folder with index files and metadata.
    """
    vectorstore.save_local(path)


def load_vector_store(embeddings, path: str = "career_agent_index"):
    """
    Load the vector store from the disc using FAISS.
    """    
    vector_path = Path(path)
    if not vector_path.exists():
        st.warning(f"Vector not found in '{path}'. Please load it first with 'Load documents'.")
        return None

    try:
        return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)
    except Exception as e:
        st.error(f"Error loading vector store: {e}")    
        return None