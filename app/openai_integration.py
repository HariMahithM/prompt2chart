import streamlit as st
import openai
import matplotlib.pyplot as plt
import pandas as pd
import re
import warnings

warnings.filterwarnings("ignore")


def handle_openai_query(df, column_names, api_tok):
    openai.api_key = api_tok

    query = st.text_area(
        "Enter your Prompt:",
        placeholder="Example: Bar plot for the first ten rows.",
    )

    if st.button("Get Answer"):
        if query.strip():
            prompt_content = f"""
            The dataset is already loaded into a DataFrame named `df`.
            Columns: {column_names}
            Use only Pandas and Matplotlib to generate plots and make the graph color more colorful and make the background black
            Prompt: {query} 
            """
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt_content},
            ]

            with st.spinner("Preparing response..."):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo", messages=messages
                )
                code = extract_code_from_markdown(response['choices'][0]['message']['content'])
                execute_openai_code(code, df)

                # Generate insights based on the query and visualization
                if code:
                    generate_insights(df, query, api_tok)


def extract_code_from_markdown(md_text):
    code_blocks = re.findall(r"```(python)?(.*?)```", md_text, re.DOTALL)
    return "\n".join([block[1].strip() for block in code_blocks])


def execute_openai_code(code, df):
    if code:
        try:
            exec(code)
            st.pyplot()
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("No valid code generated.")


def generate_insights(df, query, api_tok):
    openai.api_key = api_tok

    # Provide context for generating insights
    insight_prompt = f"""
    Based on the visualization created for the following dataset columns: {df.columns.tolist()},
    and the prompt: {query}, summarize key insights or patterns observed in the visualization in less than 100words.
    """

    messages = [
        {"role": "system", "content": "You are a helpful assistant who explains data insights."},
        {"role": "user", "content": insight_prompt},
    ]

    with st.spinner("Generating insights..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
            insights = response['choices'][0]['message']['content']
            st.subheader("Insights from Visualization ✨")
            st.write(insights)
        except Exception as e:
            st.error(f"Error in generating insights: {str(e)}")


