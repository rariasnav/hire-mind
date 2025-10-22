# 🤖 HireMind – Rafael’s Professional AI Agent

HireMind is an intelligent assistant built to analyze Rafael Arias Navarro’s GitHub repositories, technical data, and career documents using Retrieval-Augmented Generation (RAG) powered by LangChain and OpenAI.

The goal of this project is to create an AI-powered professional portfolio that provides recruiters, collaborators, or Rafael himself with insights into his technical background, experience, and skills.

## 🚀 Features

- Analyze GitHub repositories to understand Rafael’s code, technologies, and programming patterns.

- Query data-based documents (career and project information).

- Interactive chat interface for asking context-aware questions.

- Conversation memory that maintains chat context using LangChain memory buffers.

- RAG pipeline combining embeddings, vector stores, and retrieval-based reasoning.


## 🧩 Tech Stack

- Layer	Technologies
- Frontend / UI	Streamlit
- AI & LLM	OpenAI (GPT-4o-mini)
- Framework	LangChain
- Embedding & Search	FAISS
- Language	Python 3.10+


📂 Project Structure
HIRE-MIND/
├── app.py                      # Entry point for Streamlit UI
├── config.py                   
├── data/                       # PDFs and local indices
│   ├── AI-Engineer-Rafael-Arias-Navarro.pdf
│   ├── Backend-Dev-Rafael-Arias-Navarro.pdf
│   └── ...
├── modules/
│   ├── config/
│   │   └── repos.py            # GitHub repo definitions
│   ├── core/
│   │   ├── memory.py           # Conversation memory logic
│   │   └── rag_pipeline.py     # RAG chain logic
│   ├── ingestion/
│   │   ├── github_loader.py    # GitHub repo ingestion
│   │   └── pdf_loader.py       # PDF/data ingestion
│   ├── processing/
│   │   ├── embedder.py         # Embedding creation
│   │   └── vector_store.py     # Vector store management
│   └── UI/
│       ├── main_ui.py          # Main interface and layout
│       ├── github_ui.py        # GitHub loader section
│       ├── pdf_ui.py           # PDF/data loader
│       └── query_ui.py         # Chat and query interface
└──requirements.txt


## ⚙️ Setup

```bash
# 1. Clone the repo
git clone https://github.com/rariasnav/hire-mind.git
cd hiremind

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
Create a .env file in the project root with the keys:
Then add your OpenAI API key to .env
```
---

## 🧪 Run the App

```bash
streamlit run app.py
```


## 💬 Usage

Once launched, you can:

- Load one or more of Rafael’s GitHub repositories.

- Interact with the AI by asking questions like:

    “What are Rafael’s strongest programming skills?”

    “Summarize his experience in backend development.”

    “What technologies does he use most in his projects?”

The AI retrieves and summarizes data from the vectorstore to give detailed insights.

## 🧠 How It Works

- Data ingestion: GitHub repos and documents are embedded and stored in a FAISS vectorstore.

- Query processing: When the user asks a question, the relevant context is retrieved via similarity search.

- LLM reasoning: GPT-4o-mini generates a natural language answer grounded on retrieved context.

- Memory management: The assistant keeps short-term memory of recent exchanges for coherence.

👨‍💻 About the Author

Rafael Arias Navarro – Full Stack Software Developer & AI Engineer
[LinkedIn](https://www.linkedin.com/in/rafael-arias-navarro/)


💼 Experience in Python, React, Flask, Django, FastAPI, SQLAlchemy, Docker, Redis, and AI-driven SEO systems.

📄 License

This project is for demonstration and portfolio purposes only.
All personal data and content belong to Rafael Arias Navarro.