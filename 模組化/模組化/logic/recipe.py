# logic/recipe.py
import streamlit as st

class Recipe:
    def __init__(self, data: dict):
        self.name = data.get("name", "未命名食譜")
        self.ingredients = data.get("ingredients", [])
        self.prep_time = data.get("prep_time", "未指定")
        self.cook_time = data.get("cook_time", "未指定")
        self.total_time = data.get("total_time", "未指定")
        self.difficulty = data.get("difficulty", "中等")
        self.steps = data.get("steps", [])

    def render(self):
        # 確保難易度圖標正確
        difficulty_icon = {"簡單": "🟢", "中等": "🟡", "困難": "🔴"}.get(self.difficulty, "🟡")

        # 組合步驟 HTML
        steps_html = "".join([f"<li>{s.get('description','') if isinstance(s, dict) else s}</li>" for s in self.steps])

        # ⭐ 關鍵：確保這裡的 f-string 乾淨，避免因為 ingredients 內含特殊符號導致 HTML 破裂
        ingredients_str = ", ".join(self.ingredients)

        # 這裡的 unsafe_allow_html=True 是關鍵，請確保它沒有拼錯
        st.markdown(f"""
        <div class="recipe-card">
            <div class="recipe-title">{self.name}</div>
            <div class="recipe-section">
                <div class="section-title">🥬 所需食材</div>
                <div class="section-content">{ingredients_str}</div>
            </div>
            <div class="recipe-section recipe-grid">
                <div>⏱️ 準備時間：{self.prep_time}</div>
                <div>🔥 烹飪時間：{self.cook_time}</div>
                <div>⏰ 總時間：{self.total_time}</div>
                <div>{difficulty_icon} 難易度：{self.difficulty}</div>
            </div>
            <div class="recipe-section">
                <div class="section-title">👨‍🍳 詳細步驟</div>
                <div class="section-content"><ol>{steps_html}</ol></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
