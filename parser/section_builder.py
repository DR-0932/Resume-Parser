from parser.section_detector import detect_section
def build_sections(lines):
    sections = {
        "education": [],
        "experience": [],
        "projects": [],
        "skills": [],
        "achievements": [],
        "certifications": [],
        "other": []
    }

    current_section = "other"

    for line in lines:
        line = line.strip()
        if not line:
            continue

        detected = detect_section(line)
        if detected:
            current_section = detected
            continue

        sections[current_section].append(line)

    return sections
