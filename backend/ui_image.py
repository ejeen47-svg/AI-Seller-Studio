import streamlit as st
from PIL import Image

from image_prompt import make_image_prompt
from image_engine import generate_image_prompt

def show_image():

    st.header("🖼 AI 대표이미지")

    uploaded_files = st.file_uploader(
        "상품 이미지를 선택하세요",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="image_upload"
    )

    if not uploaded_files:
        return

    cols = st.columns(4)

    images = []

    for i, file in enumerate(uploaded_files):

        image = Image.open(file)

        images.append(image)

        with cols[i % 4]:
            st.image(image, use_container_width=True)

    if st.button(
        "🖼 대표이미지 프롬프트 생성",
        use_container_width=True,
        key="image_button"
    ):

        with st.spinner("AI가 프롬프트 생성중..."):

           prompt = generate_image_prompt(
           "상품 대표이미지"
)

        st.success("생성 완료")

        st.text_area(
            "AI 이미지 프롬프트",
            value=prompt,
            height=300,
            key="image_prompt_result"
        )

        st.download_button(
            "📄 프롬프트 다운로드",
            data=prompt,
            file_name="image_prompt.txt",
            mime="text/plain",
            use_container_width=True
        )