# 智慧食譜生成 App

用 Streamlit 寫的網頁應用：輸入冰箱剩下的食材，程式會呼叫語言模型生成幾道食譜，並可用 DALL-E 產生成品示意圖。

> 分組專案。**我（黃郁寧）負責程式主體**——串接 OpenAI／Gemini 生成食譜、清理並解析模型回傳、例外處理、圖片生成等；**同學負責在此基礎上改善，並重構成模組化架構**。

## 功能
- 依剩餘食材生成食譜
- 可選 OpenAI 或 Google Gemini；OpenAI 內部會自動降級備援（gpt-4o-mini → gpt-3.5-turbo）
- 可避開使用者勾選的過敏原
- 可用 DALL-E 3 生成成品示意圖

## 架構（模組化分層）
```
app.py        主進入點
ui/           畫面（版面、樣式、側欄、頁首頁尾、載入動畫）
services/     對外服務（OpenAI、Gemini、DALL-E、提示詞）
logic/        資料處理（解析、資料模型、錯誤處理）
config/       設定（常數）
```

## 執行
```bash
pip install -r requirements.txt
streamlit run app.py
# 瀏覽器開啟 http://localhost:8501，輸入 API Key 與食材
```

## 注意
- 需自備有效的 OpenAI 或 Gemini API Key（執行時於畫面輸入，未寫死在程式內）

## 作者
黃郁寧（程式主體）、同學（改善與模組化）
