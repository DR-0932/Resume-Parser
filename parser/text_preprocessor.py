import re

HEADINGS = [
    "EDUCATION",
    "WORK EXPERIENCE",
    "PROJECTS",
    "CERTIFICATES",
    "SKILLS SUMMARY",
    "ACHIEVEMENTS",
    "ADDITIONAL INFORMATION"
]

def normalize_headings(text: str) -> str:
    for heading in HEADINGS:
        # ensure heading starts on a new line
        pattern = rf"\s*({heading})\s*"
        text = re.sub(pattern, r"\n\1\n", text, flags=re.IGNORECASE)
    return text
