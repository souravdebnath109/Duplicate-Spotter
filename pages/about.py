# pages/about.py

import streamlit as st

st.title("📘 About This App")

st.markdown("""
Welcome to the **Duplicate Detection Hub** — a powerful tool designed to identify duplication across a wide range of data types with speed and accuracy.

---

### 🔍 What It Does:
This app can detect duplication or similarity in:
- 🧠 **Text & Questions** (using Semantic Similarity with Sentence-BERT + ML-based scoring)
- 🎙️ **Voice / Speaker**
- 🖼️ **Images**
- 📄 **Scanned Documents (OCR-based)**
- 📊 **Datasets / Files (CSV, Excel, JSON)**
- 📘 **Text-based PDFs**
- ✍️ **Handwritten Text**
- 🌐 **Website Text**

---

### 🛠️ How It Works:
Depending on the module, we use a combination of:
- **Transformer models (like Sentence-BERT)** for text
- **ML/DL models** for image and audio comparison
- **Feature engineering & similarity scoring**
- **OCR engines** for scanned documents
- **Hashing & embedding techniques** for files and structured data

---

### 📌 Use Cases:
- Academic plagiarism detection  
- Duplicate content detection in media  
- Dataset cleaning and deduplication  
- Document verification  
- Speaker/audio identity matching  
- Website content similarity detection  

---

### 👨‍💻 Developed By:
**Sourav Debnath**  

🔗 [GitHub](https://github.com/souravdebnath109)  
🔗 [LinkedIn](https://www.linkedin.com/in/sourav-debnath-b4a80a313/)
📅 **Version**: 1.0  
🧪 **Tech Stack**: Python · Streamlit · Transformers · scikit-learn · OpenCV · SpeechRecognition · Tesseract

---

For best experience, use the **left sidebar** to navigate between modules.
""")
