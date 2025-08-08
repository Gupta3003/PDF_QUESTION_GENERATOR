# 📄 PDF Content Extraction Web App

A Flask-based web application that allows you to **upload a PDF**, automatically **extract text and images** from each page, display them in a **clean web interface**, and save them in a **structured JSON file**.

---

## 🚀 Features

- 📤 Upload PDF via browser
- 📝 Extracts **text** and **images** from each page
- 💾 Saves images to `static/images/`
- 📁 Saves structured JSON in `output/questions.json`
- 🎨 Displays results in a responsive, styled web page
- 📑 Page numbers displayed **at the bottom** of each section

---

## 📂 Project Structure

```
pdf-extraction-web/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── static/
│   ├── css/
│   │   └── styles.css      # Custom styling
│   └── images/             # Extracted images
├── templates/
│   ├── index.html          # Upload page
│   └── results.html        # Results display page
├── uploads/                # Uploaded PDF files
└── output/
    ├── images/              # Optional extra extracted images
    └── questions.json       # Structured output data
```

---

## 🛠 Installation

1. **Clone this repository** or download the ZIP file:
   ```bash
   git clone https://github.com/yourusername/pdf-extraction-web.git
   cd pdf-extraction-web
   ```

2. **(Optional) Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶ Usage

1. **Run the Flask app**:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. **Upload a PDF** file and click **Extract Content**.

4. **View results**:
   - Text and images from each page will be displayed in the browser.
   - Page numbers are shown at the **bottom** of each section.
   - Images are saved in `static/images/`.
   - JSON output is saved in `output/questions.json`.

---

## 📦 Requirements

- Python 3.8+
- Flask
- PyMuPDF (`fitz`)
- Pillow
- Werkzeug

Install all dependencies via:
```bash
pip install -r requirements.txt
```

---

## 📌 JSON Output Example

```json
[
  {
    "page": 1,
    "text": "Q1. What comes next in the pattern?",
    "images": [
      "static/images/page1_image1.png",
      "static/images/page1_image2.png"
    ]
  },
  {
    "page": 2,
    "text": "Q2. Count the number of objects.",
    "images": [
      "static/images/page2_image1.png"
    ]
  }
]
```

---

## 🎨 UI Preview

**Upload Page:**
- Drag & drop or click to select PDF
- Blue submit button with hover effect

**Results Page:**
- Extracted text shown in readable format
- Images displayed in a responsive grid
- Page number footer at the bottom of each section

---

## 📜 License
This project is licensed under the MIT License — feel free to modify and use it.

---

## 💡 Future Enhancements
- AI-powered question generation from extracted text/images
- Support for multiple PDF uploads at once
- Search and filter within extracted content
