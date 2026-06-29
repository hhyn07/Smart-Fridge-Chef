import streamlit as st

def handle_error(e, provider):
    msg = str(e)

    if "quota" in msg or "429" in msg:
        st.error("❌ API 配額不足")
        if provider == "OpenAI":
            st.info("👉 建議切換到 Google Gemini（免費）")
    else:
        st.error(f"❌ 發生錯誤：{msg}")
