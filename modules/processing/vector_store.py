def save_vector_store(vectorstore, path="career_agent_index"):
    """
    Save the vector store to a file.
    Create a folder with index files and metadata.
    """
    vectorstore.save_local(path)

def load_vector_store(embeddings, path="career_agent_index"):
    """
    Load the vector store from the disc using FAISS."""
    from langchain_community.vectorstores import FAISS
    from pathlib import Path
    import streamlit as st
    
    vector_path = Path(path)
    if not vector_path.exists():
        st.warning(f"Vector not found in '{path}'. Please load it first with 'Load PDFs'.")
        return None
    
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)