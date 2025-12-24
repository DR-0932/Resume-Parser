import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"A:\Apps\Release-24.02.0-0\poppler-24.02.0\Library\bin"

def extract_text_with_ocr(pdf_path):
    text = ""
    images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
    for img in images:
        text += pytesseract.image_to_string(img, lang="eng") + "\n"
    return text
