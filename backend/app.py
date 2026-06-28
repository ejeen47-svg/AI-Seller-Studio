import streamlit as st
import google.generativeai as genai
from PIL import Image
import pandas as pd

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="AI Seller Studio",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 AI Seller Studio")
st.caption("사진 여러 장으로 스마트스토어·쿠팡 상품 정보를 자동 생성합니다.")

# -----------------------------
# Gemini API
# -----------------------------
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    st.error("GEMINI_API_KEY가 등록되지 않았습니다.")
    st.stop()

# -----------------------------
# 업로드
# -----------------------------
uploaded_files = st.file_uploader(
    "상품 사진을 선택하세요 (최대 10장)",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

# -----------------------------
# 처리
# -----------------------------
if uploaded_files:

    images = []

    cols = st.columns(min(len(uploaded_files), 4))

    for i, file in enumerate(uploaded_files):
        image = Image.open(file)
        images.append(image)

        with cols[i % len(cols)]:
            st.image(image, width=220)

    if st.button("🤖 AI 상품 생성", type="primary"):

        with st.spinner("AI가 상품을 분석중입니다..."):

            model = genai.GenerativeModel("gemini-2.5-flash")

            prompt = """
당신은 대한민국 최고의 스마트스토어/쿠팡 MD입니다.

사진 속 상품을 모두 분석하여 아래 형식 그대로 작성하세요.

========================

【스마트스토어 상품명】

【쿠팡 상품명】

【태그】
태그1,태그2,태그3,태그4,태그5,태그6,태그7,태그8,태그9,태그10

【색상】

【옵션】

【사이즈】

【재질】

【구성품】

【상품 특징】

- 특징1
- 특징2
- 특징3
- 특징4
- 특징5

【300자 상품설명】

========================

반드시 한국어로 작성하세요.
"""

            response = model.generate_content([prompt] + images)

            result = response.text

            st.success("생성이 완료되었습니다!")

            st.divider()

            st.subheader("📋 AI 생성 결과")

            st.text_area(
                "결과",
                value=result,
                height=500
            )

            st.download_button(
                label="📄 TXT 다운로드",
                data=result,
                file_name="상품정보.txt",
                mime="text/plain"
            )

            df = pd.DataFrame({
                "상품정보": [result]
            })

            csv = df.to_csv(index=False).encode("utf-8-sig")

            st.download_button(
                label="📊 CSV 다운로드",
                data=csv,
                file_name="상품정보.csv",
                mime="text/csv"
            )