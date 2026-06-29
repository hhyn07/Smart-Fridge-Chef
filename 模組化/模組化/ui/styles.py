import streamlit as st

# 冰箱主題樣式
def apply_styles():
    st.markdown("""
    <style>
    /* 冰箱主題背景 - 冷色調漸變 */
    .stApp {
        background: linear-gradient(135deg, #0a1929 0%, #1a2b3d 50%, #0f1b2e 100%);
        background-attachment: fixed;
    }
    
    /* 添加冰箱門的視覺效果 */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 100%;
        background: 
            repeating-linear-gradient(
                0deg,
                transparent,
                transparent 2px,
                rgba(100, 200, 255, 0.03) 2px,
                rgba(100, 200, 255, 0.03) 4px
            );
        pointer-events: none;
        z-index: 0;
    }
    
    /* 主標題 - 冰箱風格 */
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #64b5f6 0%, #42a5f5 50%, #90caf9 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 30px rgba(100, 181, 246, 0.3);
        animation: titleGlow 3s ease-in-out infinite;
        position: relative;
    }
    
    @keyframes titleGlow {
        0%, 100% { filter: brightness(1); }
        50% { filter: brightness(1.2); }
    }
    
    /* 副標題 */
    .subtitle {
        font-size: 1.1rem;
        color: #b0bec5;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 300;
        letter-spacing: 1px;
    }
    
    /* 冰箱卡片樣式 - 冷色調 */
    .recipe-card {
        background: linear-gradient(135deg, rgba(30, 50, 70, 0.9) 0%, rgba(20, 40, 60, 0.9) 100%);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        border: 2px solid rgba(100, 181, 246, 0.2);
        box-shadow: 
            0 8px 16px rgba(0, 0, 0, 0.4),
            0 0 20px rgba(100, 181, 246, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .recipe-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(100, 181, 246, 0.1), transparent);
        transition: left 0.5s;
    }
    
    .recipe-card:hover {
        transform: translateY(-5px);
        border-color: rgba(100, 181, 246, 0.4);
        box-shadow: 
            0 12px 24px rgba(0, 0, 0, 0.5),
            0 0 30px rgba(100, 181, 246, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.2);
    }
    
    .recipe-card:hover::before {
        left: 100%;
    }
    
    /* 食譜標題 - 冰藍色 */
    .recipe-title {
        font-size: 1.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #64b5f6 0%, #42a5f5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        position: relative;
    }
    .recipe-section {
        margin-bottom: 1rem;
    }
    .section-title {
        font-size: 1rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    .section-content {
        font-size: 0.9rem;
        color: #cccccc;
        line-height: 1.6;
    }
    .stTextInput > div > div > input {
        background-color: #2a2a2a;
        color: #ffffff;
        border: 1px solid #444444;
        border-radius: 8px;
    }
    /* 按鈕 - 冰箱按鈕風格 */
    .stButton > button {
        background: linear-gradient(135deg, #42a5f5 0%, #1e88e5 50%, #1565c0 100%);
        color: white;
        border: 2px solid rgba(100, 181, 246, 0.3);
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 700;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 
            0 4px 8px rgba(0, 0, 0, 0.3),
            0 0 15px rgba(66, 165, 245, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 
            0 8px 16px rgba(0, 0, 0, 0.4),
            0 0 25px rgba(66, 165, 245, 0.5);
        border-color: rgba(100, 181, 246, 0.6);
    }
    
    .stButton > button:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) scale(0.98);
    }
    /* 表格 - 冰箱風格 */
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 1rem 0;
        background: linear-gradient(135deg, rgba(30, 50, 70, 0.8) 0%, rgba(20, 40, 60, 0.8) 100%);
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid rgba(100, 181, 246, 0.2);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }
    table th, table td {
        padding: 1rem;
        text-align: left;
        border-bottom: 1px solid rgba(100, 181, 246, 0.1);
        color: #e3f2fd;
    }
    table th {
        background: linear-gradient(135deg, rgba(66, 165, 245, 0.3) 0%, rgba(30, 136, 229, 0.3) 100%);
        font-weight: 700;
        color: #64b5f6;
        text-shadow: 0 0 10px rgba(100, 181, 246, 0.5);
    }
    table tr:last-child td {
        border-bottom: none;
    }
    table tr:hover {
        background: rgba(66, 165, 245, 0.1);
        transition: background 0.3s ease;
    }
    
    /* 側邊欄樣式 */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a1929 0%, #1a2b3d 100%);
        border-right: 2px solid rgba(100, 181, 246, 0.2);
    }
    
    /* 輸入框 - 冰箱風格 */
    .stTextInput > div > div > input {
        background: rgba(30, 50, 70, 0.6);
        color: #e3f2fd;
        border: 2px solid rgba(100, 181, 246, 0.3);
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: rgba(100, 181, 246, 0.6);
        box-shadow: 0 0 15px rgba(100, 181, 246, 0.3);
        background: rgba(30, 50, 70, 0.8);
    }
    
    /* 添加浮動的雪花/冰晶裝飾 */
    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(0deg); opacity: 0.7; }
        50% { transform: translateY(-20px) rotate(180deg); opacity: 1; }
    }
    
    .snowflake {
        position: fixed;
        color: rgba(100, 181, 246, 0.3);
        font-size: 1.5rem;
        animation: float 6s ease-in-out infinite;
        pointer-events: none;
        z-index: 1;
    }
    
    /* 標題區域添加冰箱圖標動畫 */
    .fridge-icon {
        display: inline-block;
        animation: fridgeGlow 2s ease-in-out infinite;
        filter: drop-shadow(0 0 10px rgba(100, 181, 246, 0.5));
    }
    
    @keyframes fridgeGlow {
        0%, 100% { transform: scale(1); filter: drop-shadow(0 0 10px rgba(100, 181, 246, 0.5)); }
        50% { transform: scale(1.1); filter: drop-shadow(0 0 20px rgba(100, 181, 246, 0.8)); }
    }
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #64b5f6, #42a5f5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .main-title .emoji {
        -webkit-text-fill-color: initial;
    }
    [data-testid="stCaption"] p {
        text-align: center;
        font-style: italic;
        opacity: 0.8;
    }
    .ai-loading-container {
        text-align: center;
        padding: 2rem;
    }

    .ai-loading-emoji {
        font-size: 3rem;
        animation: cooking 2s ease-in-out infinite;
    }

    .ai-loading-text {
        margin-top: 1rem;
        color: #b0bec5;
        font-size: 1.1rem;
    }

    .ai-loading-bars {
        margin-top: 1rem;
    }

    .ai-loading-bar {
        display: inline-block;
        width: 40px;
        height: 4px;
        background: linear-gradient(90deg, #64b5f6, #42a5f5);
        margin: 0 4px;
        animation: loading 1.5s ease-in-out infinite;
    }

    .ai-loading-bar:nth-child(2) {
        animation-delay: 0.2s;
    }

    .ai-loading-bar:nth-child(3) {
        animation-delay: 0.4s;
    }

    @keyframes cooking {
        0%, 100% { transform: scale(1) rotate(0deg); }
        25% { transform: scale(1.1) rotate(5deg); }
        50% { transform: scale(1) rotate(0deg); }
        75% { transform: scale(1.1) rotate(-5deg); }
    }

    @keyframes loading {
        0%, 100% { opacity: 0.3; transform: scaleY(0.5); }
        50% { opacity: 1; transform: scaleY(1); }
    }
    .recipe-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 0.75rem;
        margin-top: 0.5rem;
        color: #e3f2fd;
        font-size: 0.9rem;
    }


    /* 步驟列表 */
    .recipe-card ol {
        padding-left: 1.2rem;
    }

    .recipe-card li {
        margin-bottom: 0.5rem;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)