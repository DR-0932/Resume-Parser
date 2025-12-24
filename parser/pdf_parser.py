from .ocr_extractor import extract_text_with_ocr
import fitz

def extract_text_from_pdf(pdf_path):
  text=""

  with fitz.open(pdf_path) as pdf:
    for page in pdf:
      text += page.get_text()

  if not text or len(text.strip())<200:
    text = extract_text_with_ocr(pdf_path)

    return text