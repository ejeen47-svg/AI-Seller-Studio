import streamlit as st
import google.generativeai as genai
from PIL import Image
import pandas as pd

from parser import parse_result
from price_calculator import calculate_price
from translator import translate_detail
from detail_page import make_detail_page
# --------------------------
# 페이지 설정
# --------------------------

st.set_page_config(
    page_title="AI Seller Studio",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 AI Seller Studio")
st.caption("AI가 상품을 자동 분석하여 스마트스토어와 쿠팡 등록 정보를 생성합니다.")


# --------------------------
# Gemini API
# --------------------------

try:
    genai.configure(
        api_key=st.secrets["GEMINI_API_KEY"]
    )
except Exception:

    st.error("GEMINI_API_KEY가 없습니다.")
    st.stop()


# --------------------------
# 이미지 업로드
# --------------------------

uploaded_files = st.file_uploader(
    "상품 이미지를 선택하세요 (최대 10장)",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)


images = []

if uploaded_files:

    st.subheader("📷 업로드 이미지")

    cols = st.columns(4)

    for i, file in enumerate(uploaded_files):

        image = Image.open(file)

        images.append(image)

        with cols[i % 4]:
            st.image(image, use_container_width=True)
  # --------------------------
# AI 분석
# --------------------------

if images:

    if st.button(
        "🤖 AI 상품 생성",
        type="primary",
        use_container_width=True
    ):

        with st.spinner("AI가 상품을 분석중입니다..."):

            model = genai.GenerativeModel(
                "gemini-2.5-flash"
            )

            prompt = """
당신은 대한민국 최고의 스마트스토어·쿠팡 MD입니다.

사진들을 모두 분석하여 반드시 아래 형식으로만 출력하세요.

### 스마트스토어 상품명

### 쿠팡 상품명

### 태그

### 색상

### 옵션

### 사이즈

### 재질

### 구성품

### 상품특징

### 상품설명

모든 내용은 한국어로 작성하세요.
"""

            response = model.generate_content(
                [prompt] + images
            )

            result = response.text

            data = parse_result(result)

            st.success("AI 분석 완료")

            st.divider()

# --------------------------
# 결과 출력
# --------------------------

            st.subheader("🛒 스마트스토어 상품명")

            st.text_input(
                label="스마트스토어",
                value=data["smartstore_title"],
                key="smartstore_title"
            )

            st.subheader("📦 쿠팡 상품명")

            st.text_input(
                label="쿠팡",
                value=data["coupang_title"],
                key="coupang_title"
            )

            st.subheader("🏷 태그")

            st.text_area(
                label="태그",
                value=data["tags"],
                height=120,
                key="tags"
            )

            st.subheader("🎨 색상")

            st.text_input(
                label="색상",
                value=data["color"],
                key="color"
            )

            st.subheader("⚙ 옵션")

            st.text_area(
                label="옵션",
                value=data["option"],
                height=120,
                key="option"
            )

            st.subheader("📏 사이즈")

            st.text_area(
                label="사이즈",
                value=data["size"],
                height=120,
                key="size"
            )

            st.subheader("📝 상품설명")

            st.text_area(
                label="상품설명",
                value=data["description"],
                height=300,
                key="description"
            )
  # --------------------------
# 다운로드
# --------------------------

            st.divider()

            st.subheader("📥 다운로드")

            col1, col2 = st.columns(2)

            with col1:

                st.download_button(
                    label="📄 TXT 다운로드",
                    data=result,
                    file_name="상품정보.txt",
                    mime="text/plain",
                    use_container_width=True
                )

            with col2:

                csv = pd.DataFrame({
                    "상품정보": [result]
                }).to_csv(
                    index=False
                ).encode("utf-8-sig")

                st.download_button(
                    label="📊 CSV 다운로드",
                    data=csv,
                    file_name="상품정보.csv",
                    mime="text/csv",
                    use_container_width=True
                )


# --------------------------
# 판매가 계산기
# --------------------------

st.divider()

st.header("💰 판매가 계산기")

left, right = st.columns(2)

with left:

    china_price = st.number_input(
        "중국가격(위안)",
        value=23.6
    )

    exchange_rate = st.number_input(
        "환율",
        value=200
    )

with right:

    international_shipping = st.number_input(
        "국제배송비",
        value=6000
    )

    domestic_shipping = st.number_input(
        "국내배송비",
        value=3500
    )

margin_rate = st.slider(
    "희망 마진율 (%)",
    min_value=10,
    max_value=80,
    value=30
)

if st.button(
    "💰 판매가 계산",
    use_container_width=True
):

    price = calculate_price(
        china_price,
        exchange_rate,
        international_shipping,
        domestic_shipping,
        margin_rate
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "원가",
            f"{price['원가']:,}원"
        )

        st.metric(
            "총원가",
            f"{price['총원가']:,}원"
        )

    with col2:

        st.metric(
            "권장판매가",
            f"{price['권장판매가']:,}원"
        )

        st.metric(
            "예상마진",
            f"{price['예상마진']:,}원"
        )
   # --------------------------
# 프로그램 정보
# --------------------------

st.divider()

with st.expander("ℹ 프로그램 정보"):

    st.markdown("""
### AI Seller Studio PRO

현재 버전 : **V3**

기능

- ✅ 여러 장 이미지 분석
- ✅ 스마트스토어 상품명 생성
- ✅ 쿠팡 상품명 생성
- ✅ 태그 생성
- ✅ 색상 추출
- ✅ 옵션 추출
- ✅ 사이즈 추출
- ✅ 상품설명 생성
- ✅ TXT 다운로드
- ✅ CSV 다운로드
- ✅ 판매가 계산기

개발 예정

- 중국 상세페이지 번역
- 한국형 상세페이지 생성
- 대표이미지 생성
- 글자 제거
- 스마트스토어 등록
- 쿠팡 등록
""")

st.divider()

left, right = st.columns(2)

with left:

    if st.button(
        "🔄 새로 분석하기",
        use_container_width=True,
        key="reset_ai"
    ):
        st.rerun()

with right:

    st.button(
        "🚀 다음 기능 준비중",
        use_container_width=True,
        disabled=True,
        key="next_step"
    )
# --------------------------
# 중국 상세페이지 번역
# --------------------------

st.divider()

st.header("🇨🇳 중국 상세페이지 번역")

china_text = st.text_area(
    "중국어 내용을 붙여넣으세요",
    height=250,
    key="china_text"
)

if st.button(
    "🇰🇷 한국어 번역",
    use_container_width=True,
    key="translate_button"
):

    if china_text.strip():

        with st.spinner("번역중입니다..."):

            korean = translate_detail(china_text)

            st.subheader("번역 결과")

            st.text_area(
                "한국어",
                value=korean,
                height=350,
                key="translated_text"
            )

    else:

        st.warning("중국어를 입력하세요.")
   # ---------------------------------
# AI 상세페이지 생성
# ---------------------------------

st.divider()

st.header("📝 AI 상세페이지 생성")

if st.button(
    "📝 상세페이지 만들기",
    use_container_width=True,
    key="detail_page"
):

    if images:

        with st.spinner("상세페이지 생성중입니다..."):

            detail = make_detail_page(images)

            st.subheader("생성된 상세페이지")

            st.text_area(
                "상세페이지",
                value=detail,
                height=500,
                key="detail_result"
            )

            st.download_button(
                "📄 상세페이지 TXT 다운로드",
                data=detail,
                file_name="상세페이지.txt",
                mime="text/plain",
                use_container_width=True
            )

    else:

        st.warning("먼저 상품 이미지를 업로드하세요.")     