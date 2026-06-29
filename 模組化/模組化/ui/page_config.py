# ui/page_config.py
import streamlit as st

def setup_page():
    st.set_page_config(
        page_title="AI 冰箱食譜管理員",
        page_icon="🧊",
        layout="centered",
        initial_sidebar_state="expanded"
    )
