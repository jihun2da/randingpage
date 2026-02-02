import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(page_title="기린컴퍼니 랜딩", layout="wide")

html_path = Path(__file__).parent / "landing.html"
html = html_path.read_text(encoding="utf-8")

components.html(html, height=2200, scrolling=True)
