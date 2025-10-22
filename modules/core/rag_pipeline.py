import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from modules.ingestion.pdf_loader import load_all_pdfs_from_folder
from modules.ingestion.github_loader import load_github_repos
from modules.processing.embedder import create_vector_store
from modules.processing.vector_store import save_vector_store, load_vector_store
from modules.core.memory import get_memory


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=api_key)

# ---------- CORE FUNCTIONS ----------

def initialize_vectorstore():
    """
    Tries to load the vectorstore from disk, otherwise returns None.
    """
    try:
        return load_vector_store(embeddings)
    except FileNotFoundError:
        return None


def build_from_pdfs(folder_path="data"):
    """
    Loads PDFs, builds vectorstore, saves it, and returns it.
    """
    texts = load_all_pdfs_from_folder(folder_path)
    vectorstore = create_vector_store(texts)
    save_vector_store(vectorstore)
    return vectorstore, [f.name for f in Path(folder_path).glob("*.pdf")]


def build_from_github(repos: list[str]):
    """
    Loads content from GitHub, builds vectorstore, saves it, and returns it.
    """
    repo_texts = load_github_repos(repos)
    vectorstore = create_vector_store(repo_texts)
    repo_ids = [r.replace("/", "_") for r in repos]
    save_vector_store(vectorstore, path=f"github_{'_'.join(repo_ids)}_index")
    return vectorstore, repos


def query_rag(vectorstore, query: str, memory=None):
    """
    Executes a RAG query using the vectorstore, conversation memory, and default LangChain prompt.
    """
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    
    if memory is None:
        memory = get_memory(buffer_type="window", k=5)
    
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3)
    
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
        verbose=True
    )
    
    result = chain.invoke({"question": query})
    return result