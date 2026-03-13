# 🔐 AI Cyber Threat Detection System

An AI-powered cybersecurity system that detects malicious network traffic using machine learning.

This project analyzes network traffic data and predicts potential cyber threats using the **CICIDS2017 dataset**.

---

## 🚀 Features

- AI-based cyber attack detection
- Machine learning model (Random Forest)
- Real-time prediction dashboard
- Attack statistics visualization
- Upload custom network traffic data
- Download detection results

---

## 🧠 Technologies Used

- Python
- Scikit-learn
- Pandas
- Streamlit
- Matplotlib

---



## Setup

1. Clone the repository
git clone https://github.com/manojtk900/ai-cyber-threat-detection.git

2. Create virtual environment
python -m venv venv

3. Activate environment
venv\Scripts\activate

4. Install dependencies
pip install -r requirements.txt

5. Train model
python model/train_model.py

6. Run dashboard
streamlit run app/dashboard.py

## Dataset
This project uses the CICIDS2017 dataset.

Download:
https://www.unb.ca/cic/datasets/ids-2017.html

##📂 Project Structure
ai-cyber-threat-detection
│
├── dataset
│   ├── Friday-WorkingHours-Afternoon-DDoS.pcap_ISCX.csv
│
├── model
│   ├── train_model.py
│   └── model.pkl
│
├── utils
│   └── preprocess.py
│
├── app
│   └── dashboard.py
│
├── requirements.txt
├── README.md
└── .gitignore



##📥 Dataset
This project uses the CICIDS2017 Intrusion Detection Dataset.

Download it from:
https://www.unb.ca/cic/datasets/ids-2017.html

## 📊 System Architecture

```mermaid
flowchart LR

A[Network Traffic Dataset] --> B[Data Preprocessing]
B --> C[Feature Engineering]
C --> D[Random Forest Model]
D --> E[Threat Prediction]
E --> F[Streamlit Dashboard]
F --> G[Threat Visualization]

##👨‍💻 Author

Manoj T K

AI / Machine Learning Project





