import streamlit as st
from pathlib import Path

st.set_page_config(page_title="PragyanAI", layout="wide")

# Path to image
IMAGE_PATH = Path(__file__).parent / "PragyanAI_Transperent.png"

st.title("PragyanAI")

if IMAGE_PATH.exists():
    st.image(str(IMAGE_PATH), use_container_width=True)
else:
    st.error(f"Image not found: {IMAGE_PATH}")
