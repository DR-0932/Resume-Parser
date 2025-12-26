import csv
import os

CSV_FILE = "parsed_resumes.csv"

def write_to_csv(filename, sections):
    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "filename",
                "education",
                "experience",
                "projects",
                "certifications",
                "skills",
                "other"
            ]
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "filename": filename,
            "education": " | ".join(sections.get("education", [])),
            "experience": " | ".join(sections.get("experience", [])),
            "projects": " | ".join(sections.get("projects", [])),
            "certifications": " | ".join(sections.get("certifications", [])),
            "skills": ", ".join(sections.get("skills", [])),
            "other": " | ".join(sections.get("other", [])),
        })
