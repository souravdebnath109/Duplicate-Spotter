# web_utils.py

import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def fetch_page(url, timeout=10):
    resp = requests.get(url, timeout=timeout, allow_redirects=True)
    resp.raise_for_status()
    return resp.url, resp.text

def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=" ", strip=True)
    return " ".join(text.split())

def compare_websites(url1, url2, threshold=0.9):
    try:
        final1, html1 = fetch_page(url1)
        final2, html2 = fetch_page(url2)
    except Exception as e:
        return {"error": str(e)}

    redirect_same = (final1 == final2)

    text1 = clean_html(html1)
    text2 = clean_html(html2)
    if not text1 or not text2:
        return {"redirect_same": redirect_same, "text_similarity": 0.0, "same": False}

    vect = TfidfVectorizer(stop_words="english", max_features=5000)
    mat = vect.fit_transform([text1, text2])
    score = float(cosine_similarity(mat[0:1], mat[1:2])[0][0])
    same = (score >= threshold)

    return {
        "redirect_same": redirect_same,
        "text_similarity": score,
        "same": same
    }
