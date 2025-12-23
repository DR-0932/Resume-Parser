import re

COMMON_SKILLS = [
    "python", "java", "javascript", "react", "node", "express",
    "c++", "c", "html", "css", "sql", "mongodb", "flutter",
    "git", "docker", "kubernetes", "aws", "linux",
    "machine learning", "deep learning", "nlp", "tensorflow"
]

def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in COMMON_SKILLS:
        
        pattern = re.escape(skill)

        if re.search(rf"\b{pattern}\b", text):

            found_skills.append(skill)

    return list(set(found_skills))  
