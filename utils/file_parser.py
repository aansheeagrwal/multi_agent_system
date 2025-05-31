# utils/file_parser.py

import json
import PyPDF2

def parse_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def parse_txt(file_path):
    with open(file_path, "r") as file:
        return file.read()

def parse_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)
