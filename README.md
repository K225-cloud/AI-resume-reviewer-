# AI-resume-reviewer-
Here firstly we need to import requirment libraries
#let's set up the code:

1. **Setting Up the App**:
   - We're creating a web application using Python and Flask, a framework that helps us build web applications.
   - We import necessary tools like Flask for creating the web app, render_template for handling HTML templates, request for processing user requests, pdfplumber for working with PDF files, and openai for integrating with OpenAI's API.

2. **Configuring OpenAI API**:
   - We set up our OpenAI API key (`openai.api_key = 'YOUR_OPENAI_API_KEY'`). This key allows us to access OpenAI's powerful text generation capabilities.

3. **Defining Routes**:
   - Our app has two main routes (`@app.route('/')` and `@app.route('/upload', methods=['POST'])`).
   - The `'/'` route renders the `resume.html` template, which will be our homepage with an upload form.
   - The `/upload` route handles form submissions when users upload their resume files.

4. **Handling File Uploads**:
   - When a user uploads a file (we're expecting a PDF), our app checks if it's a PDF file. If it is, we extract text from it using pdfplumber.
   - If the file isn't a PDF, we display an error message saying it's an unsupported format.

5. **Using OpenAI API**:
   - Once we have the text from the resume, we send it to OpenAI's API (`analyze_resume` function) for analysis.
   - We specify parameters like the model (`text-davinci-003`), which is a language model capable of generating human-like text.
   - here thing to remember we need to buy or purchase a model of chat gpt to use it now all the old models is not working

6. **Displaying Feedback**:
   - The feedback we get from OpenAI's analysis is then displayed to the user using the `feedback.html` template.

7. **Running the App**:
   - Finally, we run the Flask app in debug mode, which helps us detect and fix errors more easily during development.

So essentially, this code creates a web app where users can upload their resume files, and the app uses OpenAI's API to analyze the content of those resumes and provide feedback. It's a simplified example of how you can integrate text analysis and generation capabilities into a web application.
