import re

EXP_KEYWORDS = [
    "experience", "intern", "internship",
    "software engineer", "developer",
    "worked at", "work experience",
    "full stack", "backend", "frontend",
    "sde", "software development"
]

def extract_experience(lines):
    experience = []

    for line in lines:
        low = line.lower()

        
        for word in EXP_KEYWORDS:
            if word in low:
                experience.append(line.strip())
                break

        # detect years (e.g., 2019-2021, 2020 to 2023)
        if re.search(r'(20\d{2})\s*[-to]+\s*(20\d{2})', low):
            experience.append(line.strip())

    return list(set(experience))