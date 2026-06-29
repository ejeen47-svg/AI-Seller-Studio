import google.generativeai as genai


def analyze_product(images):

    prompt = """
당신은 대한민국 최고의 온라인 쇼핑몰 MD입니다.

업로드된 모든 이미지를 분석하여

아래 형식으로 작성하세요.

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

반드시 한국어만 출력하세요.
"""

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    response = model.generate_content(
        [prompt] + images
    )

    return response.text