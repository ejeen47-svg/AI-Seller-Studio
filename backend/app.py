import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(
    page_title="AI Seller Studio",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 AI Seller Studio")
st.caption("사진 한 장으로 스마트스토어·쿠팡 상품을 자동 생성합니다.")

# Gemini API Key
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except:
    st.error("GEMINI_API_KEY가 등록되지 않았습니다.")
    st.stop()

uploaded_files = st.file_uploader(
    "상품 사진을 선택하세요 (최대 10장)",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if uploaded_files:

   images = []

for file in uploaded_files:
    image = Image.open(file)
    images.append(image)
    st.image(image, width=250)
    st.image(image, width=350)

    if st.button("🤖 AI 상품 생성"):

        with st.spinner("AI가 분석중입니다..."):

            model = genai.GenerativeModel("gemini-2.5-flash")

            prompt = """
사진 속 상품을 분석하여 아래 형식으로 작성해줘.

1. 스마트스토어 상품명

2. 쿠팡 상품명

3. 태그 10개

4. 상품 특징 5가지

5. 300자 상품설명

한국어로 작성.
"""

            response = model.generate_content(
                [prompt, image]
            )

            st.success("생성 완료!")

            st.markdown(response.text)