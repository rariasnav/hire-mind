import streamlit as st
from modules.core.rag_pipeline import query_rag

    
def query_interface_ui():
    st.subheader("🔍 Ask a question about Rafael's career:")
    query = st.text_input("Ask something:")

    if query:
        if not st.session_state.vectorstore:
            st.warning("Please load or generate the vector store first.")
        else:
            with st.spinner("Analyzing..."):
                result = query_rag(
                    st.session_state.vectorstore, 
                    query, 
                    memory=st.session_state.memory
                )
                
                st.markdown("### 🧠 **Answer:**")
                if isinstance(result, dict):
                    answer = result.get("answer") or result.get("result") or result.get("output_text")
                    st.write(answer)
                else:
                    st.write(result)