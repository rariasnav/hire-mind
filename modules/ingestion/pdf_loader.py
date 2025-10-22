import PyPDF2
from pathlib import Path

def load_all_pdfs_from_folder(folder_path: str) -> list[str]:
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
        with open(pdf_file, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""
        pdf_texts.append(text.strip())
        print(f"✅ Loaded: {pdf_file.name} ({len(text)}) characters")

    return pdf_texts
