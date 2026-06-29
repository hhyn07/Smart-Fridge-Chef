# services/image_service.py

def generate_food_image(recipe_text: str) -> str:
    """
    產生料理圖片（目前為佔位版本）
    回傳圖片描述或 placeholder
    """
    if not recipe_text:
        return ""

    return (
        "https://via.placeholder.com/512x512.png?"
        "text=Food+Image+Coming+Soon"
    )
