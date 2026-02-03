import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(page_title="기린컴퍼니 랜딩 비교", layout="wide")

st.title("기린컴퍼니 랜딩페이지 버전 비교")

# 선택 옵션
pages = {
    "V1 · SaaS / Corporate": "landing_v1.html",
    "V2 · 감성 중심": "landing_v2.html",
    "V3 · 전환율 중심(CTA)": "landing_v3.html",
    "V4 · 초보자 친화": "landing_v4.html",
    "V4 · 뉴로 친화": "landing_v5.html",
}

selected = st.selectbox("확인할 랜딩페이지를 선택하세요", pages.keys())

html_path = Path(__file__).parent / pages[selected]
html = html_path.read_text(encoding="utf-8")

components.html(html, height=3600, scrolling=True)
