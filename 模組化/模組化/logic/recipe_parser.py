# logic/recipe_parser.py
import json
import re
from logic.recipe import Recipe

def parse_recipes(raw_text: str) -> list[Recipe]:
    if not raw_text or not raw_text.strip():
        raise ValueError("模型沒有回傳任何內容")

    # 清掉 ```json ``` 包裝
    cleaned = re.sub(r"```json|```", "", raw_text).strip()
    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON 解析失敗：{e}")

    return [Recipe(r) for r in data["recipes"]]
