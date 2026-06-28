import google.generativeai as genai


def make_image_prompt(detail):

    prompt = f"""
당신은 대한민국 최고의 상세페이지 디자이너입니다.

아래 상품설명을 이용하여

상세페이지 첫 번째 화면에 들어갈

이미지 생성용 프롬프트를 작성하세요.

디자인 스타일

- 화이트 배경

- 고급스러운 느낌

- 한국 쇼핑몰 스타일

- 제품 강조

- 아이콘 사용

- 읽기 쉬운 구성

상품설명

{detail}

"""

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    response = model.generate_content(
        prompt
    )

    return response.text