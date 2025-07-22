

# At the top of app.py

import base64

import streamlit as st
from helper import query_point_creator, model
from audio_utils import is_speaker_duplicate
from image_utils import is_image_duplicate
from document_utils import is_document_duplicate
from handwriting_utils import compare_handwriting

from PIL import Image
import uuid
import time
import os
import numpy as np
import streamlit as st
from pdf_utils import compare_pdfs
import streamlit as st
from PIL import Image
import numpy as np
import io

import streamlit as st
from web_utils import compare_websites


# -------------------- INIT & DEEPFACE WARM-UP --------------------
 # Ensures TensorFlow model is ready

st.set_page_config(page_title="Duplication Spotter", layout="centered")

# Sidebar Navigation
page = st.sidebar.radio(
    "Choose Task",
    [
         "🏠 Homepage",
        "Question Duplicate Checker",
        "Voice Duplicate Checker",
        "Image Duplicate Checker",
        "Image Text Duplicate Checker",
       "Dataset/File Duplicate Checker",
       "Text PDF Duplicate Checker",
       "📝 Handwriting Duplicate Checker",
        "Website Duplicate Checker",



    ]
)

# -------------------- TEXT DUPLICATION --------------------
# -------------------- HOMEPAGE --------------------
# -------------------- HOMEPAGE --------------------
if page == "🏠 Homepage":
    
    
    
    with open("images/bg.png", "rb") as f:
        img_data = base64.b64encode(f.read()).decode()

    st.markdown(f"""
        <style>
            .homepage-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                text-align: center;
                padding: 2rem 1rem;
            }}
            .homepage-title {{
                font-size: 2.8rem;
                font-weight: 800;
                color: #3b82f6;
                margin-bottom: 1rem;
            }}
            .homepage-text {{
                font-size: 1.05rem;
                font-weight: bold;
                color: #ffffff;
                max-width: 750px;
                margin-bottom: 2rem;
                line-height: 1.7;
            }}
            .homepage-footer {{
                font-size: 1rem;
                margin-top: 1rem;
                font-weight: bold;
                color: #ffffff;
            }}
            img {{
                max-width: 3200px;
                margin-bottom: 2rem;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }}
        </style>

        <div class="homepage-container">
            <div class="homepage-title">🔁 Duplication Spotter</div>
            <img src="data:image/png;base64,{img_data}" alt="Detective Image" />
            <div class="homepage-text">
                <strong>Duplicate Detection Hub</strong> quickly identifies duplicate or similar content across text, audio, images, scanned documents, datasets, PDFs, handwritten notes, and website content. <br>
                Powered by advanced AI, machine learning, and OCR, each module delivers fast, precise results—ideal for plagiarism checks, data cleaning, document matching, and media deduplication.
            </div>
            <div class="homepage-footer">
                👉 Use the <strong>sidebar</strong> to select a detection module and begin.
            </div>
        </div>
    """, unsafe_allow_html=True)


elif page == "Question Duplicate Checker":
    st.title("🧠 Text Duplicate Detection")
    q1 = st.text_input("Enter Question 1:")
    q2 = st.text_input("Enter Question 2:")

    if st.button("Check Duplication"):
        if q1 and q2:
            vec = query_point_creator(q1, q2)
            prediction = model.predict(vec)[0]
            if prediction:
                st.success("✅ The questions are likely duplicates.")
            else:
                st.warning("❌ The questions are not duplicates.")
        else:
            st.error("Please enter both questions.")

# -------------------- VOICE DUPLICATION --------------------
elif page == "Voice Duplicate Checker":
    st.title("🎙️ Voice Duplicate Detection")
    audio_file1 = st.file_uploader("Upload First Audio (.wav)", type=["wav"])
    audio_file2 = st.file_uploader("Upload Second Audio (.wav)", type=["wav"])
    threshold = st.slider("Similarity Threshold", min_value=0.0, max_value=1.0, value=0.75, step=0.01)

    if st.button("Compare Voices"):
        if audio_file1 and audio_file2:
            try:
                os.makedirs("audio_samples", exist_ok=True)
                temp1_path = os.path.join("audio_samples", f"{uuid.uuid4()}.wav")
                temp2_path = os.path.join("audio_samples", f"{uuid.uuid4()}.wav")
                with open(temp1_path, "wb") as f1:
                    f1.write(audio_file1.read())
                with open(temp2_path, "wb") as f2:
                    f2.write(audio_file2.read())
                result, score = is_speaker_duplicate(temp1_path, temp2_path, threshold=threshold)
                st.write(f"🔎 Similarity Score: `{score.item():.3f}`")
                if result:
                    st.success("✅ Both voices are from the same speaker.")
                else:
                    st.warning("❌ Voices are from different speakers.")
            except Exception as e:
                st.error(f"Error: {e}")
            finally:
                time.sleep(1)
                for f in [temp1_path, temp2_path]:
                    if os.path.exists(f):
                        os.remove(f)
        else:
            st.error("Please upload both audio files.")

# -------------------- IMAGE DUPLICATION --------------------
elif page == "Image Duplicate Checker":
    st.title("🖼️ Image Duplicate Detection")
    img_file1 = st.file_uploader("Upload First Image", type=["jpg", "jpeg", "png"], key="img1")
    img_file2 = st.file_uploader("Upload Second Image", type=["jpg", "jpeg", "png"], key="img2")
    threshold = st.slider("Hash Difference Threshold", min_value=0, max_value=64, value=5)

    if st.button("Compare Images"):
        if img_file1 and img_file2:
            img1 = Image.open(img_file1)
            img2 = Image.open(img_file2)
            result, score = is_image_duplicate(img1, img2, threshold)
            st.image([img1, img2], caption=["Image 1", "Image 2"], width=250)
            st.write(f"🔎 Hash Distance: `{score}`")
            if result:
                st.success("✅ Images are likely duplicates.")
            else:
                st.warning("❌ Images are different.")
        else:
            st.error("Please upload both images.")

# -------------------- DOCUMENT DUPLICATION --------------------
elif page == "Image Text Duplicate Checker":
    st.title("📄 Image Text Duplicate Checker")
    doc_file1 = st.file_uploader("Upload First Document Image", type=["jpg", "jpeg", "png"], key="doc1")
    doc_file2 = st.file_uploader("Upload Second Document Image", type=["jpg", "jpeg", "png"], key="doc2")
    threshold = st.slider("Text Similarity Threshold", min_value=0.0, max_value=1.0, value=0.7, step=0.01)

    if st.button("Compare Documents"):
        if doc_file1 and doc_file2:
            try:
                img1 = Image.open(doc_file1)
                img2 = Image.open(doc_file2)
                result, score = is_document_duplicate(img1, img2, threshold)
                st.image([img1, img2], caption=["Document 1", "Document 2"], width=250)
                st.write(f"🔎 OCR Text Similarity: `{score:.3f}`")
                if result:
                    st.success("✅ Documents are likely duplicates.")
                else:
                    st.warning("❌ Documents are different.")
            except Exception as e:
                st.error(f"OCR/Comparison Error: {e}")
        else:
            st.error("Please upload both document images.")
# -------------------- FILE/DATASET DUPLICATION --------------------
elif page == "Dataset/File Duplicate Checker":
    st.title("📊 Dataset/File Duplicate Detection")
    uploaded_file1 = st.file_uploader("Upload First File", type=["csv", "xlsx", "json"], key="file1")
    uploaded_file2 = st.file_uploader("Upload Second File", type=["csv", "xlsx", "json"], key="file2")
    threshold = st.slider("Row Similarity Threshold", min_value=0.0, max_value=1.0, value=0.9, step=0.01)

    if st.button("Check Dataset Duplication"):
        if uploaded_file1 and uploaded_file2:
            from file_utils import is_exact_duplicate, is_near_duplicate

            try:
                # Check for exact duplication
                if is_exact_duplicate(uploaded_file1, uploaded_file2):
                    st.success("✅ Files are *exact duplicates* (hash match).")
                else:
                    result, score = is_near_duplicate(uploaded_file1, uploaded_file2, threshold=threshold)
                    st.write(f"🔎 Row Overlap Score: `{score:.3f}`")
                    if result:
                        st.success("✅ Files are *near duplicates* (row similarity high).")
                    else:
                        st.warning("❌ Files are different.")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.error("Please upload both dataset files.")
# -------------------- TEXT PDF DUPLICATION --------------------
elif page == "Text PDF Duplicate Checker":
    st.title("📄 Text-based PDF Duplicate Checker")
    pdf_file1 = st.file_uploader("Upload First PDF", type=["pdf"], key="pdf1")
    pdf_file2 = st.file_uploader("Upload Second PDF", type=["pdf"], key="pdf2")
    threshold = st.slider("Text Similarity Threshold", min_value=0.0, max_value=1.0, value=0.8, step=0.01)

    if st.button("Compare PDFs"):
        if pdf_file1 and pdf_file2:
            from pdf_utils import compare_pdfs

            try:
                result, score = compare_pdfs(pdf_file1, pdf_file2, threshold=threshold)
                st.write(f"🔎 Cosine Similarity Score: `{score:.3f}`")
                if result:
                    st.success("✅ PDFs are likely duplicates.")
                else:
                    st.warning("❌ PDFs are different.")
            except Exception as e:
                st.error(f"Error processing PDFs: {e}")
        else:
            st.error("Please upload both PDF files.")
#--------------------- HANDWRITING DUPLICATION --------------------
elif page == "📝 Handwriting Duplicate Checker":
    st.title("📝 Handwriting Duplicate Checker (Image-based)")

    img1 = st.file_uploader("Upload First Handwritten Image", type=["jpg", "jpeg", "png"], key="hw1")
    img2 = st.file_uploader("Upload Second Handwritten Image", type=["jpg", "jpeg", "png"], key="hw2")
    threshold = st.slider("Similarity Threshold", 0.0, 1.0, 0.85, 0.01)

    if st.button("Compare Handwriting"):
        if img1 and img2:
            from handwriting_utils import compare_handwriting
            try:
                result, score = compare_handwriting(img1, img2, threshold)
                st.write(f"🔍 Cosine Similarity Score: `{score:.3f}`")
                if result:
                    st.success("✅ Handwriting samples are likely duplicates.")
                else:
                    st.warning("❌ Handwriting samples are different.")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.error("Please upload both handwriting images.")
elif page == "Website Duplicate Checker":
    st.title("🌐 Website Duplicate Checker")

    url1 = st.text_input("Enter First URL")
    url2 = st.text_input("Enter Second URL")
    threshold = st.slider("Text Similarity Threshold", 0.0, 1.0, 0.9, 0.01)

    if st.button("Compare URLs"):
        if url1 and url2:
            result = compare_websites(url1, url2, threshold)
            if "error" in result:
                st.error(f"Error: {result['error']}")
            else:
                st.write(f"🔁 Final URLs: `{result['redirect_same']}`")
                st.write(f"🔎 Text Content Similarity: `{result['text_similarity']:.3f}`")
                if result["redirect_same"]:
                    st.success("✅ Both URLs redirect to the same page.")
                elif result["same"]:
                    st.success("✅ Page content is nearly identical.")
                else:
                    st.warning("❌ Pages are different.")
        else:
            st.error("Please enter both URLs.")
