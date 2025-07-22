
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


<img width="1365" height="611" alt="Screenshot 2025-07-22 150747" src="https://github.com/user-attachments/assets/583f2afd-fa6a-4e43-9769-fbeb957ae674" />
<img width="1139" height="608" alt="Screenshot 2025-07-22 150805" src="https://github.com/user-attachments/assets/898f6636-a7b9-47c5-a191-32a446eb3449" />
<img width="1365" height="602" alt="Screenshot 2025-07-22 150823" src="https://github.com/user-attachments/assets/6843b00f-4004-4702-810e-ebc41b2e0336" />
<img width="1134" height="612" alt="Screenshot 2025-07-22 151025" src="https://github.com/user-attachments/assets/589d7941-a2c6-48c9-9ede-8ff2dc1641eb" />
<img width="1365" height="610" alt="Screenshot 2025-07-22 151038" src="https://github.com/user-attachments/assets/41332e9a-8d3f-4c42-b973-1f1bdfc4eb4c" />
<img width="1365" height="596" alt="Screenshot 2025-07-22 151315" src="https://github.com/user-attachments/assets/39df00c6-5c61-4023-8c49-30b4314cd93f" />
<img width="1142" height="604" alt="Screenshot 2025-07-22 151204" src="https://github.com/user-attachments/assets/e17afead-8524-44c7-93cc-3050af72079d" />
<img width="1365" height="601" alt="Screenshot 2025-07-22 151247" src="https://github.com/user-attachments/assets/27d0418e-96b7-4c4c-b0f7-4016e9867cb0" />
<img width="1365" height="612" alt="Screenshot 2025-07-22 151354" src="https://github.com/user-attachments/assets/b165c19b-80af-4dfc-a3cf-55f2fa9510f8" />
<img width="1365" height="607" alt="Screenshot 2025-07-22 151420" src="https://github.com/user-attachments/assets/ca646e47-cfd9-4124-b663-dac0344980b0" />
<img width="1365" height="613" alt="Screenshot 2025-07-22 151427" src="https://github.com/user-attachments/assets/04cb2304-a996-4015-b7de-6609d76730af" />
<img width="1365" height="613" alt="Screenshot 2025-07-22 151427" src="https://github.com/user-attachments/assets/f7904a3b-9555-43ad-b0ed-41d1df690f3e" />
<img width="1365" height="606" alt="Screenshot 2025-07-22 151451" src="https://github.com/user-attachments/assets/0ee78354-6291-4eb7-af56-a4bd086d122a" />
<img width="1365" height="606" alt="Screenshot 2025-07-22 151510" src="https://github.com/user-attachments/assets/bd519c1d-516d-4606-b293-1429411c835d" />
<img width="1365" height="607" alt="Screenshot 2025-07-22 151617" src="https://github.com/user-attachments/assets/02e9984c-9674-4825-b0ff-abe1587344b1" />
<img width="1145" height="610" alt="Screenshot 2025-07-22 151638" src="https://github.com/user-attachments/assets/472fba11-693b-4991-828a-ed6d3f9121e1" />
<img width="1143" height="491" alt="Screenshot 2025-07-22 151658" src="https://github.com/user-attachments/assets/8be2ffd3-48e8-4ae3-b7d0-c3364918034a" />
<img width="1100" height="610" alt="Screenshot 2025-07-22 151716" src="https://github.com/user-attachments/assets/a9a78363-153c-40af-98da-f49ac397b45f" />


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
