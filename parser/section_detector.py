SECTION_KEYWORDS = {
    "education": [
        "education", "academic", "qualification"
    ],
    "experience": [
        "experience", "work experience", "employment", "internship"
    ],
    "projects": [
        "projects", "project", "project experience", "project work"
    ],
    "skills": [
        "skills", "technical skills", "skills summary", "skill set"
    ],
    "achievements": [
        "achievements", "accomplishments"
    ],
    "certifications": [
        "certification", "certifications", "certificate"
    ]
}

def detect_section(line: str):
    l = line.lower().strip()

    # remove trailing colon or symbols
    l = l.rstrip(":").strip()

    for section, keywords in SECTION_KEYWORDS.items():
        for kw in keywords:
            # KEY CHANGE: prefix match
            if l.startswith(kw):
                return section

    return None
