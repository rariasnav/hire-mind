import streamlit as st
from modules.core.rag_pipeline import query_rag

    
def query_interface_ui():
    """
    UI component to ask questions using the RAG pipeline.
    """
    st.subheader("🔍 Ask a question about Rafael's career:")
    query = st.text_input("Ask something:")

    if query:
        if "vectorstore" not in st.session_state or st.session_state.vectorstore is None:
            st.warning("Please load or generate the vector store first.")
        else:
            if memory not in st.session_state:
                st.warning("Memory not initialized. Please ensure memory is set up.")
                return

            with st.spinner("Analyzing..."):
                try:                    
                    result = query_rag(
                        st.session_state.vectorstore, 
                        query, 
                        memory=st.session_state.memory
                    )
                
                    st.markdown("### 🧠 **Answer:**")
                    if isinstance(result, dict):
                        answer = result.get("answer") or result.get("result") or result.get("output_text")
                        st.write(answer if answer else "No answer found.")
                    else:
                        st.write(result if result else "No answer found.")
                except Exception as e:
                    st.error(f"Error during query: {e}")