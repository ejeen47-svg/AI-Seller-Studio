import streamlit as st
from PIL import Image

from detail_page import make_detail_page


def show_detail():

    st.header("📝 AI 상세페이지 생성")

    uploaded_files = st.file_uploader(
        "상품 이미지를 선택하세요",
        type=["jpg","jpeg","png"],
        accept_multiple_files=True,
        key="detail_upload"
    )

    if not uploaded_files:
        return

    images=[]

    cols=st.columns(4)

    for i,file in enumerate(uploaded_files):

        image=Image.open(file)

        images.append(image)

        with cols[i%4]:
            st.image(image,use_container_width=True)

    if st.button(
        "📝 상세페이지 생성",
        use_container_width=True,
        key="detail_button"
    ):

        with st.spinner("AI가 상세페이지 작성중입니다..."):

            detail=make_detail_page(images)

        st.success("생성 완료")

        st.text_area(
            "상세페이지",
            detail,
            height=600,
            key="detail_result"
        )

        st.download_button(
            "📄 TXT 다운로드",
            detail,
            file_name="상세페이지.txt",
            mime="text/plain",
            use_container_width=True
        )