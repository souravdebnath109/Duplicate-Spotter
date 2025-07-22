# pdf_utils.py

import fitz  # PyMuPDF
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def compare_pdfs(file1, file2, threshold=0.8):
    text1 = clean_text(extract_text_from_pdf(file1))
    file1.seek(0)
    text2 = clean_text(extract_text_from_pdf(file2))

    if not text1 or not text2:
        return False, 0.0

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    return score >= threshold, score
