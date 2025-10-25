import streamlit as st
from modules.config.repos import AVAILABLE_REPOS
from modules.core.rag_pipeline import build_from_github


def github_loader_ui():
    """
    UI component to load GitHub repositories and build the vector store.
    """
    st.subheader("💻 Load GitHub Repos")

    selected_labels = st.multiselect(
        "Select one or more projects from Rafael Arias’s portfolio to include in HireMind’s knowledge base. The AI will use this code to answer questions about his skills, development style, and project architecture.",
        options=list(AVAILABLE_REPOS.keys()),
        help="Choose one or more of Rafael's projects to include."
    )

    if vectorstore in st.session_state:
        st.warning("Data already loaded. To reload, please restart the app.")
        return

    if st.button("Load Selected Repos") and selected_labels:
        selected_repos = [AVAILABLE_REPOS[label] for label in selected_labels]
        with st.spinner("Fetching repositories..."):
            try:
                vectorstore, loaded_repos = build_from_github(selected_repos)
                st.session_state.vectorstore = vectorstore
                st.success(f"✅ Successfully loaded {len(loaded_repos)} repos: {', '.join(selected_labels)}")
            except Exception as e:
                st.error(f"Error loading repositories: {e}")

