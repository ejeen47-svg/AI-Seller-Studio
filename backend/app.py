if st.button("🤖 AI 상품 생성"):

    with st.spinner("AI가 분석중입니다..."):

        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = """
사진 속 상품들을 모두 분석하여 반드시 아래 형식만 출력하세요.

### 스마트스토어 상품명
(한 줄)

### 쿠팡 상품명
(한 줄)

### 태그
태그1,태그2,태그3,태그4,태그5,태그6,태그7,태그8,태그9,태그10

### 색상
...

### 옵션
...

### 사이즈
...

### 재질
...

### 구성품
...

### 상품특징
- 특징1
- 특징2
- 특징3
- 특징4
- 특징5

### 상품설명
300자 정도 작성.

반드시 위 형식 그대로 출력.
"""

        response = model.generate_content(
            [prompt] + images
        )

        st.success("생성 완료!")

        result = response.text

        st.subheader("📋 AI 생성 결과")

        st.text_area(
            "결과",
            value=result,
            height=500
        )