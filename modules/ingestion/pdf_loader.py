import PyPDF2
from pathlib import Path
from typing import List

def load_all_pdfs_from_folder(folder_path: str) -> List[str]:
    """
    Load and extract text from all the PDFs in a folder.
    Returns a list with the content of each PDF.
    """
    folder = Path(folder_path)
    if not folder.exists():
        raise FileNotFoundError(f"File not found {folder_path}")
    
    pdf_texts = []

    for pdf_file in folder.glob("*.pdf"):    
        text = ""
        try:
            with open(pdf_file, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    text += page.extract_text() or ""
            pdf_texts.append(text.strip())
            print(f"✅ Loaded: {pdf_file.name} ({len(text)} characters)")
        except Exception as e:
            print(f"❌ Error reading {pdf_file.name}: {e}")

    return pdf_texts
