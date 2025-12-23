import re

PROJECT_KEYWORDS = [
    "project", "built", "developed", "created", "designed",
    "github", ".git", "implementation"
]

def extract_projects(lines):
    projects = []

    for line in lines:
        low = line.lower()

        for word in PROJECT_KEYWORDS:
            if word in low:
                projects.append(line.strip())
                break

        # detect GitHub URLs specifically
        if "github.com" in low:
            projects.append(line.strip())

    return projects
