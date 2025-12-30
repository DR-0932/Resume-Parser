# RESUME PARSER

#### VIDEO DEMO
URL: https://youtu.be/H9eNR0cCYqs

#### DESCRIPTION

## What is this?
This project is a Resume Parser created as my final project for CS50. The main purpose of this project is to take a resume in PDF format, extract useful information from it, 
and convert that information into a structured CSV file. Resumes are typically designed for humans to read, not for computers to process, which makes automatic extraction difficult. 
This project focuses on solving that problem by transforming unstructured resume text into structured data that can be easily analyzed or stored.

## Project's Working....
The project begins by allowing a user to upload a resume in PDF format. Once the file is uploaded, the backend extracts raw text from the PDF. PDF files do not store text cleanly or consistently, 
so the extracted content often contains unnecessary line breaks, irregular spacing, and formatting artifacts. To address this, the project includes a text preprocessing step 
that cleans and normalizes the extracted text before any meaningful analysis is performed.

After cleaning the text, the program attempts to identify important sections of the resume. These sections include the candidate’s name, contact information such as email address and phone number,
skills, education, and work experience. Because resumes vary widely in structure and formatting, the project does not rely on a single fixed template. Instead, it uses simple rule-based logic and 
keyword matching to detect commonly used section headings and patterns. This approach is not perfect.

All extracted information is written into a single CSV file. I intentionally decided not to generate multiple CSV files for different sections such as skills or education. 
While multiple files might be useful in more advanced systems, they also add complexity and make the project harder to understand and debug. By using one CSV file, the output remains simple.

The project is implemented primarily in Python. Flask is used to handle file uploads and route requests from the user to the backend logic. Separate Python files are used to keep the code organized and modular.
This separation of responsibilities makes the code easier to read, maintain, and extend. <img width="245" height="160" alt="image" src="https://github.com/user-attachments/assets/48374f15-0fc6-4eed-863f-cbf73e1babcf" />

## Files and what they do..
  ** app.py ** 
  app.py is the main file of the project that contains the application setup and request-handling logic. It does tasks such as accepting user input (for example, an uploaded PDF), 
  calling the required processing modules in the correct sequence, managing the data flow, and generating the final output like a structured CSV file or response. 
  This file contains the code that connects all parts of the project and controls how the application runs from start to finish.

** extract_text.py **
This file contains the logic for extracting raw text from uploaded PDF resumes. It handles reading the PDF file and converting its contents into plain text that can be further processed by other modules.

** text_preprocessor.py **
This file contains functions for cleaning and normalizing the extracted text. It handles tasks such as removing unnecessary characters, standardizing formatting, and preparing the text so that section detection works more reliably.

** section_detector.py **
This file contains the logic for identifying different resume sections based on headings. It detects where sections like education, experience, and skills begin and end using predefined patterns

** section_builder.py **
This file contains the code that organizes the detected sections into a structured format. It uses regular expressions and rules to group related lines of text under the correct resume sections.

** skill_extractor.py **
This file contains the logic for extracting skills from the resume text. It matches resume content against a hardcoded list of skills, making this section more accurate and consistent compared to others.

** csv_writer.py **
This file contains the functionality for writing the processed and structured resume data into a CSV file. It ensures that all extracted information is stored in a clean, organized format as a single output file.




## Design Changes...
Initially, the idea was to use a machine learning model to train it to identify resume layout, fonts, keywords, and other patterns, and then generate suggestions and a score based on the data.
Due to time constraints and the overall complexity of this approach, I decided to postpone this implementation for a future version of the project.
Working with the PDF format also turned out to be more difficult than initially anticipated, especially when dealing with inconsistent layouts and text extraction issues.
As the project evolved, the section builder logic shifted from a planned ML-based approach to a more rule-based system using regular expressions to reliably identify and separate different resume sections.

At the current stage, the skills section is the most accurate part of the parser, since the values that can appear in this section are hardcoded and easier to match consistently. In addition to these changes,
Several other changes were made, such as simplifying the overall data flow, standardizing the output into a single CSV file instead of multiple files, and modularizing the codebase to 
make future enhancements like: adding machine learning models which are easier to integrate.

One of the main challenges encountered during development was handling the variability of resume formats. Some resumes clearly label sections like “Skills” or “Education”
while others rely on visual layout rather than explicit headings.

## Current Limitations
1. It does not use advanced natural language processing(NLP) or machine learning techniques, and it may not perform well on highly graphical or unusually formatted resumes.
2. It's unable to detect and store any type of font information used in the resume. 
3. The output does not contain any data on which section is segmented first or last in the resume.
4. The skill extraction section's scope is limited.


