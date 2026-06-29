import streamlit as st
from PIL import Image

from ocr_reader import read_chinese
from translator import translate_detail


def show_translate():

    st.header("🇨🇳 OCR 자동 번역")

    uploaded_files = st.file_uploader(
        "중국 상세페이지 이미지를 선택하세요",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="translate_upload"
    )

    if not uploaded_files:
        return

    images = []

    cols = st.columns(4)

    for i, file in enumerate(uploaded_files):

        image = Image.open(file)

        images.append(image)

        with cols[i % 4]:
            st.image(image, use_container_width=True)

    if st.button(
        "🤖 OCR + 자동번역",
        use_container_width=True,
        key="translate_button"
    ):

        with st.spinner("AI 분석중..."):

            chinese = read_chinese(images)

            korean = translate_detail(chinese)

        st.subheader("중국어")

        st.text_area(
            "",
            chinese,
            height=250,
            key="china_result"
        )

        st.subheader("한국어")

        st.text_area(
            "",
            korean,
            height=350,
            key="korea_result"
        )