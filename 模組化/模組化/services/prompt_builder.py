def build_recipe_prompt(ingredients, allergens):
    allergen_text = ""
    if allergens:
        allergen_text = f"請避免以下過敏原：{', '.join(allergens)}"

    return f"""
    根據以下食材：{ingredients}{allergen_text}

    請提供 3 道創意食譜。每道食譜需包含：
    1. 料理名稱（中文）
    2. 所需食材清單（詳細列出所有食材和調味料）
    3. 準備時間（例如：10分鐘）
    4. 烹飪時間（例如：20分鐘）
    5. 總時間（準備時間 + 烹飪時間）
    6. 難易度（簡單/中等/困難）
    7. 詳細烹飪步驟（至少 5 步，每步要詳細說明）

    請以 JSON 格式回覆，格式如下：
    {{
        "recipes": [
            {{
                "name": "料理名稱",
                "ingredients": ["食材1", "食材2", "調味料1"],
                "prep_time": "準備時間（例如：10分鐘）",
                "cook_time": "烹飪時間（例如：20分鐘）",
                "total_time": "總時間（例如：30分鐘）",
                "difficulty": "難易度（簡單/中等/困難）",
                "steps": [
                    {{
                        "step_number": 1,
                        "description": "詳細步驟說明"
                    }},
                    {{
                        "step_number": 2,
                        "description": "詳細步驟說明"
                    }}
                ]
            }}
        ]
    }}
    """