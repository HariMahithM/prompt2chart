import streamlit as st
import pandas as pd

def get_data():
    file_types = ["csv", "xlsx", "xls"]
    uploaded_file = st.file_uploader("Upload a data file", type=file_types)

    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            return pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith((".xlsx", ".xls")):
            return pd.read_excel(uploaded_file)
    return None
