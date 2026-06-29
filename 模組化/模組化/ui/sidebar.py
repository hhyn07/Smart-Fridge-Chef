import streamlit as st
from config.constants import ALLERGEN_OPTIONS

def render_sidebar():
    with st.sidebar:  # ⭐ 一定要在這裡
        st.markdown("### 🚫 過敏原過濾")
        st.markdown("選擇需要排除的過敏原，AI 將生成不含這些食材的食譜")
    
        selected_allergens = st.multiselect(
            "選擇過敏原",
            ALLERGEN_OPTIONS
        )
        st.markdown("---")
        st.markdown("### 💡 使用提示")
        st.markdown("""
        <div style="background: rgba(30, 50, 70, 0.5); padding: 1rem; border-radius: 10px; 
                    border-left: 4px solid #64b5f6;">
            <div style="color: #b0bec5; line-height: 1.8;">
            ❄️ 輸入剩餘食材，用逗號分隔<br>
            🧊 選擇需要排除的過敏原<br>
            ✨ AI 將生成 3 道創意食譜<br>
            🎯 食譜包含詳細步驟和難易度
            </div>
        </div>
        """,unsafe_allow_html=True)
    return selected_allergens
