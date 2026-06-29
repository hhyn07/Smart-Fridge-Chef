from openai import OpenAI
from services.prompt_builder import build_recipe_prompt

def generate_recipes_openai(api_key, ingredients, allergens):
    client = OpenAI(api_key=api_key)

    prompt = build_recipe_prompt(ingredients, allergens)

    for model in ["gpt-4o-mini", "gpt-3.5-turbo"]:
        try:
            res = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": "你是一位專業的料理顧問，擅長根據現有食材創造美味食譜。"
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.8
            )

            return res.choices[0].message.content, model

        except Exception:
            continue

    raise RuntimeError("❌ OpenAI 模型不可用")
