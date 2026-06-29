# ui/header.py
import streamlit as st

def render_header():
    st.markdown(
    """
    <h1 class="main-title">
        <span class="emoji">🧊</span>
        AI 冰箱食譜管理員
        <span class="emoji">🧊</span>
    </h1>
    """,
    unsafe_allow_html=True
    )
    st.divider()
