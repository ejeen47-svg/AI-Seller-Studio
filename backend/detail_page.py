import google.generativeai as genai


def make_detail_page(images):

    prompt = """
당신은 대한민국 최고의 온라인 쇼핑몰 MD입니다.

업로드된 상품 이미지를 모두 분석하여
한국형 상세페이지를 작성하세요.

다음 형식으로 작성합니다.

# 상품소개

# 상품 특징
- 특징 1
- 특징 2
- 특징 3
- 특징 4
- 특징 5

# 제품 장점

# 사용 방법

# 주의사항

# 제품 사양

# 구성품

# 마무리 설명

모든 내용은 자연스러운 한국어로 작성하세요.
"""

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    response = model.generate_content(
        [prompt] + images
    )

    return response.text