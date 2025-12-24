from flask import Flask, request,jsonify # what is request
from parser.pdf_parser import extract_text_from_pdf
from parser.text_cleaner import clean_text
from parser.skill_extractor import extract_skills
from parser.basic_info import extract_email, extract_phone_number, extract_name
from parser.education_extractor import extract_education
from parser.experience_extractor import extract_experience
from parser.projects_extractor import extract_projects
from parser.section_classifier import classify_sentence
from parser.text_extractor import extract_text_from_pdf
import os 

app = Flask(__name__)

UPLOAD_FOLDER ="uploads" 
ALLOWED_EXTENSIONS = {'pdf','docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

def allowed_file(filename):
  
  return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS 


@app.route('/uploads',methods = ['POST'])
def upload_file():

    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type"}), 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    extracted_text = extract_text_from_pdf(filepath)
    cleaned_text = clean_text(extracted_text)
    lines = cleaned_text.split("\n")

    # Extract features
    skills = extract_skills(cleaned_text)

    email = extract_email(cleaned_text)
    phone = extract_phone_number(cleaned_text)
    name = extract_name(lines)
    education = extract_education(lines)
    experience = extract_experience(lines)
    projects = extract_projects(lines)

    # ML Section Classifier
    sections = {
        "education": [],
        "experience": [],
        "skills": [],
        "projects": [],
        "other": []
    }

    raw_text = extract_text_from_pdf(filepath)
    cleaned_text = clean_text(raw_text)
    lines = cleaned_text.split("\n")

    


@app.route('/')

def home():
  return "Server running 1 2 3 ..."

if __name__ == '__main__':
  
  app.run(debug=True)

