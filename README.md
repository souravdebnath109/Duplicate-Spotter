
# 🕵️‍♂️ Duplication Spotter

**Duplication Spotter** is an intelligent Streamlit-based web app that can identify **duplicate content across multiple formats** including text, audio, image, handwriting, PDF, websites, and more. Built after learning foundational **Natural Language Processing (NLP)** from [this YouTube playlist](https://www.youtube.com/watch?v=zlUpTlaxAKI&list=PLKnIA16_RmvZo7fp5kkIth6nRTeQQsjfX), this project uses real-world data and ML models to reach **~80% accuracy in detecting duplicate questions**, and expands into other media modalities.


-----
## 🔥 Live Demo
 🔗 [Live App on Streamlit Share / Hugging Face Spaces / Render] *(Add your live app link here if hosted)*

 ----------
 
##  📺 Demo Video

[![Watch the video]https://github.com/user-attachments/assets/8d070b6c-e043-4782-b8d9-c7e82e67d3e5

-----
## 📦 Features

| Feature | Description |
|--------|-------------|
| 🧠 **Duplicate Question Detector** | Trained on Quora Q&A pairs with ~80% accuracy. Detects if two input questions are similar. |
| 🎙 **Voice Duplicate Checker** | Upload two `.wav` files and find out if they belong to the same speaker. |
| 🖼 **Image Duplicate Checker** | Compares two images and tells whether they are identical or visually different. |
| 🔤 **Image Text Duplicate Checker** | Extracts and compares text content from two images. |
| 📊 **Dataset/File Duplicate Checker** | Upload any two files (CSV, XLSX, TXT, etc.) to check if they contain the same data. |
| 📄 **Text PDF Duplicate Checker** | Compare content of two text-based PDF files for duplication. |
| ✍️ **Handwriting Duplicate Checker** | Upload two handwriting samples as images and determine if they are from the same writer. |
| 🌐 **Website Duplicate Checker** | Checks if two websites/URLs redirect to the same final page. |

---

## 🧠 How I Built It


- ✅ Learned NLP basics from this amazing [YouTube playlist](https://www.youtube.com/watch?v=zlUpTlaxAKI&list=PLKnIA16_RmvZo7fp5kkIth6nRTeQQsjfX)
- ✅ Trained a **duplicate question model** using Quora question pairs dataset
- ✅ Integrated multiple ML tools for voice, image, file, and website comparisons
- ✅ Built an interactive frontend using **Streamlit**

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/souravdebnath109/Duplicate-Spotter.git
```
````
cd Detection-Spotter
`````

### Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
# On Windows: venv\Scripts\activate

````
### Install dependencies

pip install -r requirements.txt

### Run the Streamlit app

````
streamlit run app.py
`````



## 📁 Project Structure
```
Detection-Spotter/
│
├── app.py                        # Main Streamlit app
├── model/                        # ML models and preprocessing
├── utils/                        # Helper functions (text, audio, image, etc.)
├── images/                       # Sample images and icons
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
````
## 📷 Screenshots


<img width="1365" height="606" alt="Screenshot 2025-07-22 150730" src="https://github.com/user-attachments/assets/6234d1e9-e727-4016-8cb0-2226e1160ac3" />

<img width="1139" height="608" alt="Screenshot 2025-07-22 150805" src="https://github.com/user-attachments/assets/95a5fd6f-5310-43a3-9b65-8ab0551f330a" />
<img width="1365" height="610" alt="Screenshot 2025-07-22 151038" src="https://github.com/user-attachments/assets/0daa0b3e-cf50-49c7-8f3e-f6c8ba39f4ba" />

<img width="1365" height="596" alt="Screenshot 2025-07-22 151315" src="https://github.com/user-attachments/assets/62d7e3a8-5f55-47af-a46f-59f8f4a8427f" />

<img width="1142" height="604" alt="Screenshot 2025-07-22 151204" src="https://github.com/user-attachments/assets/2596ab37-195c-44db-9195-0a449ed32a58" />
<img width="1365" height="601" alt="Screenshot 2025-07-22 151247" src="https://github.com/user-attachments/assets/e4c02aa0-71e4-4946-8245-0337198bd393" />
<img width="1365" height="612" alt="Screenshot 2025-07-22 151354" src="https://github.com/user-attachments/assets/c1e271d5-2f82-4bfe-a9e7-5b85ec04cbdd" />
<img width="1365" height="607" alt="Screenshot 2025-07-22 151420" src="https://github.com/user-attachments/assets/16b1ab97-cbc5-4533-9fe6-186668ee5ae4" />
<img width="1365" height="606" alt="Screenshot 2025-07-22 151451" src="https://github.com/user-attachments/assets/8493f204-7a2c-4964-b14a-7d4cb029ecc4" />
<img width="1145" height="610" alt="Screenshot 2025-07-22 151638" src="https://github.com/user-attachments/assets/06b0fb1d-f645-42f9-b271-414d5e86f360" />
<img width="1143" height="491" alt="Screenshot 2025-07-22 151658" src="https://github.com/user-attachments/assets/8c8e9a87-dba7-401e-a42e-a455f9e7e9ae" />
<img width="1100" height="610" alt="Screenshot 2025-07-22 151716" src="https://github.com/user-attachments/assets/56310236-cbe8-4c71-8745-ce8f91f57f98" />


## 💡 Use Cases

- Plagiarism detection for education and research

- Checking similar questions in forums

- Voice or speaker verification

- Checking if two images or handwriting are duplicates

- Website redirection similarity

- File and dataset version comparison
## 📌 To Do / Improvements

 - Add drag-and-drop support

 - Deploy to Hugging Face or Streamlit Community Cloud

 - Improve model accuracy and UI

 - Add login/authentication for user-specific history
## 🙏 Acknowledgements

NLP basics from:Campusx : https://www.youtube.com/watch?v=zlUpTlaxAKI&list=PLKnIA16_RmvZo7fp5kkIth6nRTeQQsjfX

Dataset: Quora Question Pairs :  https://www.kaggle.com/datasets/quora/question-pairs-dataset

Tools: 
```
scikit-learn, streamlit, speechbrain, Pillow, pdfminer.six, tesseract, OpenCV, etc.
```
## 📬 Contact
---
#### Sourav Debnath
------
#### Email: souravdebnath54474@gamil.com
------
#### GitHub: https://github.com/souravdebnath109
----
