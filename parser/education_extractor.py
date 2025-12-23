import re

EDU_KEYWORDS = [
    "b.tech", "btech", "b.e", "be", "bachelor", "bs", "b.sc", "bsc",
    "m.tech", "mtech", "master", "ms", "m.sc", "msc",
    "high school", "secondary", "senior secondary",
    "12th", "10th", "diploma"
]

def extract_education(lines):
    education = []

    for line in lines:
        low = line.lower()

        for word in EDU_KEYWORDS:
            if word in low:
                education.append(line.strip())
                break

    return education
