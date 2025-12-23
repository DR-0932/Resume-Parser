import re

def clean_text(text):
    # Normalize encoding safely
    text = text.encode("utf-8", "ignore").decode("utf-8")

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Remove extra spaces but KEEP newlines
    text = re.sub(r'[ \t]+', ' ', text)

    # Collapse multiple newlines into one
    text = re.sub(r'\n{2,}', '\n', text)

    # Fix space before punctuation
    text = re.sub(r'\s([,.!?:])', r'\1', text)

    return text.strip()
