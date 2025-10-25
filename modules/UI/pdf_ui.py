import streamlit as st
from modules.core.rag_pipeline import build_from_pdfs

def pdf_loader_ui():
    """
    UI component to load PDFs from the 'data' folder and build the vector store.
    """
    st.subheader("📄 Data about Rafael")        
    
    if "vectorstore" in st.session_state:
        st.warning("Data already loaded. To reload, please restart the app.")

    if st.button("Load data"):
        with st.spinner("Processing and generating embeddings..."):
            try:
                vectorstore, pdf_files = build_from_pdfs("data")
                st.session_state.vectorstore = vectorstore
                st.success(f"{len(pdf_files)} data processed: {', '.join(pdf_files)}")
            except Exception as e:
                st.error(f"Error loading data: {e}")