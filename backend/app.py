import streamlit as st
from openai import OpenAI
from PIL import Image
import base64
import io

# =====================================
# 페이지 설정
# =====================================
st.set_page_config(
    page_title="AI Seller Studio",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 AI Seller Studio")
st.caption("사진 한 장으로 스마트스토어·쿠팡 상품 정보를 자동 생성합니다.")

# =====================================
# OpenAI API
# =====================================
try:
    client = OpenAI(
        api_key=st.secrets["OPENAI_API_KEY"]
    )
except Exception:
    st.error("❌ OPENAI_API_KEY가 Streamlit Secrets에 등록되어 있지 않습니다.")
    st.stop()

# =====================================
# 이미지 업로드
# =====================================
uploaded_file = st.file_uploader(
    "상품 사진을 선택하세요",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="업로드한 이미지", width=450)

    buffered = io.BytesIO()
    image.save(buffered, format="PNG")

    img_base64 = base64.b64encode(
        buffered.getvalue()
    ).decode("utf-8")

    if st.button("🤖 AI 상품 생성", use_container_width=True):

        with st.spinner("AI가 상품을 분석하는 중입니다..."):

            try:

                response = client.responses.create(
                    model="gpt-4.1-mini",
                    input=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "input_text",
                                    "text": """
너는 스마트스토어와 쿠팡 전문 MD이다.

사진을 분석하여 아래 형식으로 작성해라.

① 스마트스토어 상품명

② 쿠팡 상품명

③ 태그 10개

④ 상품 특징 5가지

⑤ 300자 상품설명

출력은 보기 좋게 작성한다.
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

                st.success("생성 완료!")

                st.markdown(result)

            except Exception as e:

                st.error("오류가 발생했습니다.")

                st.code(str(e))