# ui/loading.py
import streamlit as st
from contextlib import contextmanager
from config.constants import WARM_QUOTES
import random

@contextmanager
def show_loading():
    placeholder = st.empty()

    with placeholder.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        selected_quote = random.choice(WARM_QUOTES)
        with col2:
            st.markdown(f"""
            <div class="ai-loading-container">
                <div class="ai-loading-text">
                    {selected_quote}
                </div>
                <div class="ai-loading-bars">
                    <span class="ai-loading-bar"></span>
                    <span class="ai-loading-bar"></span>
                    <span class="ai-loading-bar"></span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    try:
        yield
    finally:
        placeholder.empty()
