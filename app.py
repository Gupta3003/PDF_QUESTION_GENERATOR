# app.py 
import os
import fitz  # PyMuPDF
import json
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "uploads"
IMAGE_FOLDER = "static/images"
OUTPUT_JSON = "output/questions.json"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(IMAGE_FOLDER, exist_ok=True)
os.makedirs("output", exist_ok=True)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def extract_pdf_content(pdf_path):
    doc = fitz.open(pdf_path)
    output = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        image_list = page.get_images(full=True)

        image_paths = []
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = f"page{page_num+1}_image{img_index+1}.{image_ext}"
            image_path = os.path.join(IMAGE_FOLDER, image_filename)

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(image_path)

        output.append({
            "page": page_num + 1,
            "text": text.strip(),
            "images": image_paths
        })

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    return output

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["pdf_file"]
        if file and file.filename.endswith(".pdf"):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            extracted_data = extract_pdf_content(filepath)
            return render_template("results.html", data=extracted_data)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
