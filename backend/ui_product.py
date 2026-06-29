import streamlit as st
from PIL import Image

from parser import parse_result
from product_engine import analyze_product


def show_product():

    st.header("📦 AI 상품분석")

    uploaded_files = st.file_uploader(
        "상품 이미지를 선택하세요",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="product_upload"
    )

    if not uploaded_files:
        st.info("상품 이미지를 업로드하세요.")
        return

    images = []

    cols = st.columns(4)

    for i, file in enumerate(uploaded_files):

        image = Image.open(file)

        images.append(image)

        with cols[i % 4]:
            st.image(
                image,
                use_container_width=True
            )

    if st.button(
        "🤖 AI 상품 생성",
        key="product_button",
        use_container_width=True
    ):

        with st.spinner("AI 분석중..."):

            result = analyze_product(images)

            data = parse_result(result)

        st.success("생성 완료")

        st.subheader("🛒 스마트스토어 상품명")

        st.text_input(
            "",
            value=data["smartstore_title"],
            key="smart_title"
        )

        st.subheader("📦 쿠팡 상품명")

        st.text_input(
            "",
            value=data["coupang_title"],
            key="coupang_title"
        )

        st.subheader("🏷 태그")

        st.text_area(
            "",
            value=data["tags"],
            height=120,
            key="tags"
        )

        st.subheader("🎨 색상")

        st.text_input(
            "",
            value=data["color"],
            key="color"
        )

        st.subheader("⚙ 옵션")

        st.text_area(
            "",
            value=data["option"],
            height=120,
            key="option"
        )

        st.subheader("📏 사이즈")

        st.text_area(
            "",
            value=data["size"],
            height=120,
            key="size"
        )

        st.subheader("📦 구성품")

        st.text_area(
            "",
            value=data["components"],
            height=120,
            key="components"
        )

        st.subheader("⭐ 상품특징")

        st.text_area(
            "",
            value=data["features"],
            height=220,
            key="features"
        )

        st.subheader("📝 상품설명")

        st.text_area(
            "",
            value=data["description"],
            height=350,
            key="description"
        )