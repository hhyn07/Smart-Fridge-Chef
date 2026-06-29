# services/gemini_service.py
import google.genai as genai
from services.prompt_builder import build_recipe_prompt

def generate_recipes_gemini(api_key, ingredients, allergens):
    genai.configure(api_key=api_key)

    prompt = build_recipe_prompt(ingredients, allergens)

    # 建議使用穩定模型
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            temperature=0.8
        )
    )

    if not response.text:
        raise RuntimeError("Gemini 回傳空內容")

    return response.text, "gemini-1.5-flash"