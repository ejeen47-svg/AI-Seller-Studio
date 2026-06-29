import streamlit as st

from price_calculator import calculate_price


def show_price():

    st.header("💰 AI 판매가 계산기")

    col1, col2 = st.columns(2)

    with col1:

        china_price = st.number_input(
            "중국가격(위안)",
            value=23.6,
            key="china_price"
        )

        exchange_rate = st.number_input(
            "환율",
            value=200,
            key="exchange_rate"
        )

        margin = st.slider(
            "희망 마진율",
            10,
            80,
            30,
            key="margin"
        )

    with col2:

        international = st.number_input(
            "국제배송비",
            value=6000,
            key="international"
        )

        domestic = st.number_input(
            "국내배송비",
            value=3500,
            key="domestic"
        )

    if st.button(
        "💰 판매가 계산",
        use_container_width=True,
        key="price_button"
    ):

        price = calculate_price(
            china_price,
            exchange_rate,
            international,
            domestic,
            margin
        )

        st.success(f"원가 : {price['원가']:,}원")
        st.success(f"총원가 : {price['총원가']:,}원")
        st.success(f"권장판매가 : {price['권장판매가']:,}원")
        st.success(f"예상마진 : {price['예상마진']:,}원")