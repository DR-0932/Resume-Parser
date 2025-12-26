from flask import Flask, request, jsonify,render_template
import os

from parser.extract_text import extract_text_from_pdf
from parser.section_builder import build_sections
from parser.csv_writer import write_to_csv
from parser.text_preprocessor import normalize_headings
from parser.skill_extractor import extract_skills
from flask import send_file


app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file"}), 400

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    # 1. Extract text
    raw_text = extract_text_from_pdf(path)

    # 2. Normalize headings BEFORE sectioning
    normalized_text = normalize_headings(raw_text)
    lines = normalized_text.split("\n")

    # 3. Build sections
    sections = build_sections(lines)

    # 4. Extract skills from multiple sections
    skill_text = " ".join(
        sections.get("skills", []) +
        sections.get("projects", []) +
        sections.get("experience", []) +
        sections.get("certifications", [])
    )

    sections["skills"] = extract_skills(skill_text)

    # 5. Write CSV ONCE
    write_to_csv(file.filename, sections)

    return jsonify(sections), 200
    
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download")
def download_csv():
    return send_file(
        "parsed_resumes.csv",
        as_attachment=True,
        download_name="parsed_resumes.csv"
    )
if __name__ == "__main__":
    app.run(debug=True)
