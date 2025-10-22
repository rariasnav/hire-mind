import streamlit as st
from modules.core.rag_pipeline import build_from_pdfs

def pdf_loader_ui():
    st.subheader("📄 Data about Rafael")        
    if st.button("Load data"):
        with st.spinner("Processing and generating embeddings..."):
            vectorstore, pdf_files = build_from_pdfs("data")
            st.session_state.vectorstore = vectorstore
        st.success(f"{len(pdf_files)} data processed: {', '.join(pdf_files)}")