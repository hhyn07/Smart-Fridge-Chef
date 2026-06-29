# Smart Fridge Chef｜智慧食譜生成 App

大三下「人工智慧程式設計與 Python」期末專題。輸入冰箱剩下的食材，程式會呼叫語言模型生成幾道食譜，並可用 DALL-E 產生成品示意圖。

> 程式碼在 `模組化/模組化/` 資料夾內。

## 功能
- 依剩餘食材生成食譜
- 可選 OpenAI 或 Google Gemini（OpenAI 會自動降級備援）
- 可避開勾選的過敏原
- 可用 DALL-E 生成成品示意圖

## 執行

```
cd 模組化/模組化
pip install -r requirements.txt
streamlit run app.py
```

## 技術
Python、Streamlit、OpenAI、Google Gemini、DALL-E

## 作者
黃郁寧（程式主體）、張乃文（改善與模組化）、林岑鎂
