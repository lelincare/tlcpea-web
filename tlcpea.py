# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 20:30:32 2026

@author: jen55
"""

import streamlit as st
import base64

# ==========================================
# 1. 網頁基本設定
# ==========================================
st.set_page_config(
    page_title="臺南市長期照顧職能培力協會 - 籌備會正式公告", 
    page_icon="🌱",
    layout="centered" 
)

# ==========================================
# 2. 進階視覺裝潢 (自定義 CSS)
# ==========================================
def inject_custom_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@500;700;900&display=swap');

        /* 整體背景色 */
        .stApp {
            background-color: #FDFCF9;
        }

        /* 全域字體 */
        html, body, [class*="css"], .stMarkdown {
            font-family: 'Noto Serif TC', serif !important;
        }

        /* 頁首標題區美化 */
        .header-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 30px 0;
            margin-bottom: 10px;
            text-align: center;
        }
        
        .association-name {
            color: #2D4F1E;
            font-size: 40px !important;
            font-weight: 900 !important;
            margin-top: 20px !important;
            margin-bottom: 10px !important;
            letter-spacing: 2px;
            line-height: 1.2;
        }
        
        .subtitle {
            color: #8C6D4A;
            font-size: 24px !important;
            font-weight: 700 !important;
            letter-spacing: 4px;
            border-top: 2px solid #EAE0D5;
            border-bottom: 2px solid #EAE0D5;
            padding: 8px 20px;
            margin-top: 10px !important;
        }

        /* 大公告標題 */
        .notice-main-title {
            color: #556B2F;
            font-size: 32px !important;
            font-weight: 700 !important;
            text-align: center;
            margin-top: 40px;
            margin-bottom: 25px;
            position: relative;
            display: inline-block;
            left: 50%;
            transform: translateX(-50%);
        }
        .notice-main-title:after {
            content: '';
            display: block;
            width: 80px;
            height: 4px;
            background: #8C6D4A;
            margin: 10px auto 0;
            border-radius: 2px;
        }

        /* 卡片排版美化 */
        .section-card {
            padding: 30px 35px;
            border-radius: 16px;
            margin-bottom: 20px;
            line-height: 1.9;
            color: #333333;
            box-shadow: 0 10px 25px rgba(45, 79, 30, 0.05); 
            transition: transform 0.3s ease;
        }
        .section-card:hover {
            transform: translateY(-3px);
        }

        .bg-green {
            background-color: #F6FAF5;
            border: 1px solid #E2ECD8;
            border-top: 4px solid #2D4F1E;
        }

        .bg-white {
            background-color: #FFFFFF;
            border: 1px solid #F0EAE3;
        }

        .bg-earth {
            background-color: #FDF9F5;
            border: 1px solid #F2E8DC;
            border-top: 4px solid #8C6D4A;
        }

        .section-card strong {
            color: #2D4F1E;
            font-weight: 700;
        }
        
        .item-number {
            color: #8C6D4A;
            font-weight: 900;
            font-size: 1.1em;
            margin-right: 5px;
        }

        .highlight-name {
            background-color: #E2ECD8;
            padding: 3px 10px;
            border-radius: 6px;
            color: #2D4F1E;
            font-weight: 700;
            margin: 0 2px;
        }

        .contact-list {
            margin-left: 15px;
            margin-top: 15px;
            list-style-type: none;
        }
        .contact-list li {
            margin-bottom: 12px;
            position: relative;
            padding-left: 30px;
        }
        .contact-list li:before {
            content: "🌿";
            position: absolute;
            left: 0;
            color: #556B2F;
        }
        
        /* 【修正】結尾虛線框：改為靠左對齊 */
        .action-call {
            text-align: left; /* 這裡原本是 center，已改為 left */
            border: 2px dashed #EAE0D5;
            background-color: #FFFFFF;
            color: #2D4F1E;
            font-weight: 700;
        }

        </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. 圖片處理函數
# ==========================================
def get_image_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def main():
    inject_custom_css()

    logo_filename = "協會logo.png" 
    banner_filename = "banner.jpg" 

    try:
        logo_base64 = get_image_base64(logo_filename)
        logo_html = f'<img src="data:image/png;base64,{logo_base64}" width="180">'
    except FileNotFoundError:
        logo_html = '<span style="font-size: 80px;">🌱</span>' 

    # --- 1. 頁首標題區 ---
    st.markdown(f"""
<div class="header-container">
    {logo_html}
    <div class="association-name">臺南市長期照顧職能培力協會</div>
    <div class="subtitle">籌備處官方公告專區</div>
</div>
    """, unsafe_allow_html=True)

    # --- 2. 形象橫幅圖片區 ---
    try:
        # 【修正】將 use_column_width 改為最新支援的 use_container_width，消除黃色警告
        st.image(banner_filename, use_container_width=True)
    except FileNotFoundError:
        st.write("---") 

    # --- 3. 公告主體 ---
    st.markdown('<div class="notice-main-title">公開徵求招募會員</div>', unsafe_allow_html=True)

    # --- 公告內容 ---
    st.markdown(f"""
<div class="section-card bg-green">
    <strong>主旨：</strong> 發起人 <span class="highlight-name">蔡孟儒</span> 已經向臺南市政府社會局提出申請籌組「臺南市長期照顧職能培力協會」社會團體，茲公開徵求會員。
</div>

<div style="font-weight: 700; color: #556B2F; font-size: 22px; margin: 35px 0 15px 10px; text-align:center; letter-spacing:2px;">【 公告事項 】</div>

<div class="section-card bg-white" style="border-left: 5px solid #EAE0D5;">
    <span class="item-number">一、</span><strong>社會團體宗旨：</strong><br>
    <div style="padding-left: 25px; margin-top: 10px; color: #444; font-size: 1.05em;">
        本會為依法設立、非以營利為目的之公益性社會團體，以結合社會各界資源，提升長期照顧服務品質，培力專業照顧人才，並推動長照產業之永續發展為宗旨。
    </div>
</div>

<div class="section-card bg-earth">
    <span class="item-number">二、</span><strong>入會資格：</strong><br>
    凡贊同本會宗旨，年滿十八歲，於臺南市從事長照相關工作或對此領域有興趣之民眾。
</div>

<div class="section-card bg-white">
    <span class="item-number">三、</span><strong>申請期間：</strong><br>
    自中華民國 <strong>115 年 4 月 1 日</strong>起，至 <strong>115 年 4 月 10 日</strong>止。
</div>

<div class="section-card bg-green">
    <span class="item-number">四、</span><strong>聯絡方式：</strong>
    <ul class="contact-list">
        <li><strong>地址：</strong> 臺南市佳里區中興街22號1樓</li>
        <li><strong>電子信箱：</strong> tlcpea.tw@gmail.com </li>
    </ul>
    <div style="margin-top: 20px; padding-top: 15px; border-top: 1px solid #DCE7D5;">
        <span class="item-number">五、</span><strong>籌備會聯絡人、電話：</strong><br>
        蔡孟儒 先生 <strong style="font-size: 1.2em; letter-spacing:1px;">0918-633886</strong>
    </div>
</div>

<div class="section-card action-call">
    <span class="item-number">六、</span>入會申請資料如附，請來電（信）索取。
</div>

<div style="text-align: right; font-weight: 900; color: #2D4F1E; font-size: 24px; margin-top: 40px; margin-right: 15px; letter-spacing: 1px;">
    發起人代表： 蔡孟儒
</div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()