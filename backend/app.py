import streamlit as st

st.set_page_config(
    page_title="AI Seller Studio",
    page_icon="🛒"
)

st.title("🛒 AI Seller Studio")

st.write("사진 한 장으로 스마트스토어·쿠팡 상품을 자동 생성합니다.")

image = st.file_uploader(
    "상품 사진을 선택하세요",
    type=["jpg", "jpeg", "png"]
)

if image:
    st.image(image, caption="업로드한 사진")
    st.success("사진 업로드 완료!")

    if st.button("✨ 상품명 생성"):
        st.success("상품명 생성 완료!")
        st.write("스테인리스 벽선반 304 벽걸이 선반 주방 선반")