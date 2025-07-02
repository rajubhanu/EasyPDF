from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/pdf-to-word', methods=['POST'])
def pdf_to_word():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    
    # Save uploaded PDF temporarily
    input_path = 'input.pdf'
    file.save(input_path)

    # Dummy processing: just send back the same file renamed as output.docx
    output_path = 'output.docx'
    os.rename(input_path, output_path)

    # Send the output file back
    return send_file(output_path, as_attachment=True, download_name="converted.docx")

if __name__ == "__main__":
    app.run(debug=True)
