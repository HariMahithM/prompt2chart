import streamlit as st
from utils import display_app_header
from data_handling import get_data
from openai_integration import handle_openai_query
import pandas as pd
import warnings


warnings.filterwarnings("ignore")



display_app_header()

with st.expander("App Overview", expanded=False):
    st.markdown(
        """
        - **Upload your data** and provide a prompt to generate visualizations.
        - **Supported formats:** CSV, XLS, XLSX.
        """
    )

# API Key
API_KEY = "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" 

# Upload data
df = get_data()

if df is not None:
    with st.expander("Show data"):
        st.write(df)

    column_names = ", ".join(df.columns)

    if not df.empty:
        handle_openai_query(df, column_names, API_KEY)
    else:
        st.warning("The uploaded data is empty.")
else:
    st.info("Please upload a dataset to begin.")
