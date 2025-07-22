# document_utils.py
import pytesseract
from PIL import Image
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text(image):
    return pytesseract.image_to_string(image)

def is_document_duplicate(img1, img2, threshold=0.7):
    """Compare OCR texts from two images"""
    text1 = extract_text(img1)
    text2 = extract_text(img2)

    if not text1.strip() or not text2.strip():
        raise ValueError("One or both documents are unreadable.")

    vectorizer = TfidfVectorizer().fit_transform([text1, text2])
    sim_score = cosine_similarity(vectorizer[0], vectorizer[1])[0][0]
    return sim_score >= threshold, sim_score
