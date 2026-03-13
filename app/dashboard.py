import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("model/model.pkl", "rb"))

st.title("AI Cyber Threat Detection System")

file = st.file_uploader("Upload Network Traffic Dataset (.csv)")

if file:

    # Load dataset
    data = pd.read_csv(file)

    # Clean column names
    data.columns = data.columns.str.strip()

    # Remove label column if present
    if "Label" in data.columns:
        data = data.drop("Label", axis=1)

    # Replace infinity values
    data.replace([np.inf, -np.inf], np.nan, inplace=True)

    # Fill missing values
    data.fillna(0, inplace=True)

    # Model prediction
    prediction = model.predict(data)

    data["Prediction"] = prediction

    st.subheader("Detection Results")
    st.write(data)

    # Attack summary
    attacks = data[data["Prediction"] == 1]

    st.subheader("Detected Threats")
    st.write(attacks)

    st.subheader("Attack Distribution")

    chart_data = data["Prediction"].value_counts()

    st.bar_chart(chart_data)

    # Dashboard metrics
    st.subheader("Threat Summary")

    total = len(data)
    attack_count = len(attacks)
    normal_count = total - attack_count

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", total)
    col2.metric("Detected Attacks", attack_count)
    col3.metric("Normal Traffic", normal_count)

    #Threat Percentage
    attack_percent = (attack_count / total) * 100

    st.metric("Attack Percentage", f"{attack_percent:.2f}%")

    #Threat Percentage
    csv = data.to_csv(index=False)

    st.download_button(
    "Download Detection Results",
    csv,
    "threat_results.csv",
    "text/csv"
    )
    