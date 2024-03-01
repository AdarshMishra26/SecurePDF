from flask import Flask, render_template, request, send_file
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return render_template('index.html', error='No file uploaded')
        
        file = request.files['file']
        
        # Check if file is empty
        if file.filename == '':
            return render_template('index.html', error='No selected file')
        
        # Check if the file is a PDF
        if file.filename[-3:].lower() != 'pdf':
            return render_template('index.html', error='File is not a PDF')
        
        # Get the password from the form
        password = request.form['password']
        
        # Encrypt the PDF
        encrypted_pdf = encrypt_pdf(file, password)
        
        # Return the encrypted PDF
        return send_file(encrypted_pdf, mimetype='application/pdf', as_attachment=True, download_name='encrypted_file.pdf')
    
    return render_template('index.html', error=None)

def encrypt_pdf(file, password):
    pdf_reader = PdfReader(file)
    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    # Encrypt the PDF with the provided password
    pdf_writer.encrypt(password)

    # Write the encrypted PDF to a BytesIO object
    encrypted_pdf_stream = BytesIO()
    pdf_writer.write(encrypted_pdf_stream)
    encrypted_pdf_stream.seek(0)

    return encrypted_pdf_stream

if __name__ == '__main__':
    app.run(debug=True)
