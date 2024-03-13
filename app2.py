from flask import Flask, render_template, request
import os
import openai
import pdfplumber


app = Flask(__name__)

# Configure OpenAI API
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('resume.html')

@app.route('/upload', methods=['POST'])

def upload_resume():
    resume_file = request.files['resume']
    if resume_file.filename.endswith('.pdf'):
        resume_text = extract_text_from_pdf(resume_file)
        feedback = analyze_resume(resume_text)
        return render_template('feedback.html', feedback=feedback)
    else:
        return 'Unsupported file format. Please upload a PDF file.'

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text


def analyze_resume(resume_text):
    # Call OpenAI API to analyze resume
    response = openai.Completion.create(
        engine="whisper-1",
        prompt=resume_text,
        max_tokens=150,
        temperature=0.7,
        stop=["\n"]
    )
    return response.choices[0].text.strip()
if __name__ == '__main__':
    app.run(debug=True)
    
    
