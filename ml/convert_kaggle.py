import pandas as pd
import re

# Load Kaggle dataset
df = pd.read_csv("ml/raw_kaggle/Resume.csv")

output = []

def split_into_lines(text):
    # Replace bullets with newline
    text = text.replace("•", "\n").replace("*", "\n")
    # Convert multiple newlines to one
    text = re.sub(r"\n+", "\n", text)
    # Split by newline or period
    parts = re.split(r"[\n\.]", text)
    return [p.strip() for p in parts if p.strip()]

def guess_label(line):
    l = line.lower()

    # EDUCATION
    if any(k in l for k in ["b.tech", "btech", "b.e", "b.sc", "msc", "m.tech", "bachelor", "master", "graduated"]):
        return "education"

    # EXPERIENCE
    if any(k in l for k in ["experience", "intern", "developer", "engineer", "worked", "company", "manager"]):
        return "experience"

    # SKILLS
    if any(k in l for k in [
        "python", "java", "sql", "c++", "html", "css", "javascript", 
        "machine learning", "react", "node", "flask", "django"
    ]):
        return "skills"

    # PROJECTS
    if any(k in l for k in ["project", "built", "developed", "created", "implemented"]):
        return "project"

    return "other"


for index, row in df.iterrows():
    resume = str(row["Resume"])
    lines = split_into_lines(resume)

    for line in lines:
        label = guess_label(line)
        output.append({"sentence": line, "label": label})

# Save converted dataset
result = pd.DataFrame(output)
result.to_csv("ml/kaggle_converted_dataset.csv", index=False)

print("Conversion complete ✔ Created kaggle_converted_dataset.csv")
