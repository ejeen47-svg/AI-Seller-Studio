import streamlit as st

from ui_home import show_home
from ui_product import show_product
from ui_translate import show_translate
from ui_detail import show_detail
from ui_image import show_image
from ui_price import show_price

st.set_page_config(
    page_title="AI Seller Studio PRO",
    page_icon="🛒",
    layout="wide"
)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 홈",
    "📦 상품분석",
    "🇨🇳 OCR 번역",
    "📝 상세페이지",
    "🖼 대표이미지",
    "💰 판매가"
])
with tab1:
    show_home()

with tab2:
    show_product()

with tab3:
    show_translate()  

with tab4:
    show_detail()   

with tab5:
    show_image()   

with tab6:
    show_price()   