import re

def extract_email(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.search(pattern, text)
    return emails.group(0) if emails else None


def extract_phone_number(text):
    pattern = r'\+?\d[\d -]{8,}\d'
    phone_numbers = re.search(pattern, text)
    return phone_numbers.group(0) if phone_numbers else None

def extract_name(lines):
    for line in lines[:10]:   
        clean = line.strip()

        if not clean:
            continue

        # only letters and spaces
        if not clean.replace(" ", "").isalpha():
            continue

        parts = clean.split()
        if 2 <= len(parts) <= 4:
            return clean

    return None