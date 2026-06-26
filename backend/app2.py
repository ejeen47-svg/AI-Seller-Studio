import streamlit as st
from openai import OpenAI
import base64
from PIL import Image
import io

# ===========================
# OpenAI API
# ===========================
client = OpenAI(
    api_key="여기에_본인의_API_KEY"
)

# ===========================
# 페이지 설정
# ===========================
st.set_page_config(
    page_title="AI Seller Studio",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 AI Seller Studio")
st.caption("사진 한 장으로 스마트스토어·쿠팡 상품 정보를 자동 생성합니다.")

uploaded_file = st.file_uploader(
    "상품 사진을 선택하세요",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, width=400)

    buffered = io.BytesIO()
    image.save(buffered, format="PNG")

    img_base64 = base64.b64encode(
        buffered.getvalue()
    ).decode()
        if st.button("🤖 AI 상품 생성"):

        with st.spinner("AI가 상품을 분석하는 중입니다..."):

            response = client.responses.create(
                model="gpt-4.1-mini",
                input=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "input_text",
                                "text": """
사진 속 상품을 분석해서 아래 형식으로 작성해줘.

1. 스마트스토어 상품명
2. 쿠팡 상품명
3. 태그 10개
4. 상품 특징 5가지
5. 300자 상품설명
"""
                            },
                            {
                                "type": "input_image",
                                "image_url": f"data:image/png;base64,{img_base64}"
                            }
                        ]
                    }
                ]
            )

            result = response.output_text