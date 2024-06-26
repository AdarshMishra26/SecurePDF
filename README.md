# PDF Encryption Web App

This Flask-based web application allows users to upload PDF files and encrypt them using a password provided via a form. Upon encryption, the encrypted PDF is returned for download.

## Features
- Upload PDF files securely.
- Encrypt uploaded PDF files with a password.
- Download the encrypted PDF file.

## Installation and Setup
1. **Clone the repository:**
    ```
    git clone https://github.com/AdarshMishra26/SecurePDF.git
    ```
   
2. **Navigate to the project directory:**
    ```
    cd pdf-encryption-web-app
    ```

3. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

4. **Run the Flask application:**
    ```
    python app.py
    ```

5. **Open a web browser and visit** `http://localhost:5000` **to access the application.**

## Usage
1. Upload a PDF file by clicking on the "Choose File" button.
2. Enter a password in the provided field.
3. Click on the "Encrypt PDF" button.
4. Download the encrypted PDF file.

## Files
- **app.py**: Contains the Flask application code with routes for file upload, encryption, and rendering HTML templates.
- **index.html**: HTML template for the file upload page.
- **README.md**: Documentation for the project.
- **requirements.txt**: List of dependencies required to run the application.

## Dependencies
- Flask
- PyPDF2

## Contributors
- [Adarsh Mishra](https://github.com/adarshmishra26)


