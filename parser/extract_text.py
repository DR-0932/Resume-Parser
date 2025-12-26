import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""

    with fitz.open(pdf_path) as doc:
        for page in doc:
            page_text = page.get_text()
            if page_text:
                text += page_text + "\n"

    return text
