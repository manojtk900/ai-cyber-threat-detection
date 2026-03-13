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
