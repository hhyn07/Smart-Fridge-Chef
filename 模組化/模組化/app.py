import streamlit as st

from ui.page_config import setup_page
from ui.styles import apply_styles
from ui.sidebar import render_sidebar
from ui.header import render_header
from ui.footer import render_footer
from ui.loading import show_loading

from services.prompt_builder import build_recipe_prompt
from services.openai_service import generate_recipes_openai
from services.gemini_service import generate_recipes_gemini
from services.image_service import generate_food_image

from logic.recipe_parser import parse_recipes
from logic.error_handler import handle_error

setup_page()
apply_styles()

selected_allergens = render_sidebar()  # ⭐ 永遠在最前面
render_header()

api_provider = st.radio(
    "選擇 AI 服務提供商",
    ["OpenAI", "Google Gemini (免費額度)"]
)

api_key = st.text_input("API Key", type="password")
ingredients = st.text_input("🥬 剩餘食材")

generate_image = (
    st.checkbox("🖼️ 生成圖片", value=True)
    if api_provider == "OpenAI"
    else False
)

if st.button("✨ 生成食譜"):
    try:
        with show_loading():
            if api_provider == "OpenAI":
                raw_text, model = generate_recipes_openai(
                    api_key,
                    ingredients,
                    selected_allergens
                )
            else:
                raw_text, model = generate_recipes_gemini(
                    api_key,
                    ingredients,
                    selected_allergens
                )

        st.success(f"🤖 使用模型：{model}")
        st.markdown("## 📝 推薦食譜")

        recipes = parse_recipes(raw_text)

        for recipe in recipes:
            recipe.render()

    except Exception as e:
        handle_error(e, api_provider)

render_footer()
