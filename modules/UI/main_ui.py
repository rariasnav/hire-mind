import streamlit as st
from modules.UI.pdf_ui import pdf_loader_ui
from modules.UI.github_ui import github_loader_ui
from modules.UI.query_ui import query_interface_ui
from modules.core.rag_pipeline import initialize_vectorstore

def main_ui():
    st.set_page_config(page_title="HireMind - Rafael's AI Agent", page_icon="🤖")
    st.title("🤖 HireMind - Rafael's Professional AI Agent")
    
    st.markdown("""
    ### Welcome to HireMind!
    HireMind is an intelligent assistant designed to analyze **GitHub repositories**, **technical documents**, and **job-related PDFs**
    to help recruiters, collaborators, or Rafael himself understand his **skills, experience, and technical background**.

    **What you can do here:**
    - Load one or more of Rafael’s GitHub repositories to let the AI analyze his code and projects.
    - Access curated **data** that provides additional professional context.
    - 💬 Ask questions like:
        - “What are Rafael’s strongest programming skills?”  
        - “Summarize his experience in backend development.”  
        - “What technologies does he use most in his projects?”

    **Goal:** Provide a transparent and AI-powered overview of Rafael’s professional profile.
    """)
    
    # Initialize vectorstore
    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = initialize_vectorstore()
        if st.session_state.vectorstore:
            st.success("Vector store loaded from disk.")
        else:
            st.info("No vector store found. Please load data first.")
            
    if "memory" not in st.session_state:
        from modules.core.memory import get_memory
        st.session_state.memory = get_memory(buffer_type="window", k=5)
            
    # --- Render sections ---
    pdf_loader_ui()
    github_loader_ui()
    query_interface_ui()   