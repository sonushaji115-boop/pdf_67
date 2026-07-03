import streamlit as st
from pathlib import Path

st.set_page_config(page_title="PragyanAI", layout="wide")

st.title("PragyanAI")

# Image in the same folder as app.py
image_path = Path(__file__).parent / "PragyanAI_Transperent.png"

if image_path.is_file():
    st.image(image_path, use_container_width=True)
else:
    st.error(f"Image not found: {image_path}")
