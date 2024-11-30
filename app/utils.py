import streamlit as st
import base64

def display_app_header(logo_dark="data/logo.png", logo_light="data/2log.png", subtitle=None):

    st.markdown(
        """
        <script>
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            localStorage.setItem('theme', 'dark');
        } else {
            localStorage.setItem('theme', 'light');
        }
        </script>
        """,
        unsafe_allow_html=True,
    )


    theme = "dark" if st.session_state.get('theme', 'dark') == 'dark' else 'light'
    logo_path = logo_dark if theme == 'dark' else logo_light


    st.markdown(
        """
        <style>
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 10px 0;
            border-bottom: 2px solid #ddd;
        }
        .header-logo {
            max-width: 20px;
            margin-right: 20px;
        }
        .header-text {
            font-size: 24px;
            font-weight: bold;
            color: #333;
        }
        .header-subtitle {
            font-size: 16px;
            color: #666;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="header-container">
            <img src="data:image/png;base64,{convert_image_to_base64(logo_path)}" class="header-logo" />
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        "***Transform your data into stunning visualizations with a single prompt!** Upload your dataset, describe the chart you need, and let the app handle the rest — '**powered by AI and Python.**'*"
    )

def convert_image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")
