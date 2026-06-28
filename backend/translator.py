import google.generativeai as genai


def translate_detail(text):

    prompt = f"""
당신은 대한민국 최고의 온라인 쇼핑몰 MD입니다.

아래 중국어 상품설명을

1. 자연스러운 한국어로 번역하고

2. 한국 쇼핑몰 스타일로 수정하고

3. 광고성 문구는 제거하고

4. 고객이 이해하기 쉽게 작성하세요.

------------------------

{text}

------------------------

한국어만 출력하세요.
"""

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    response = model.generate_content(prompt)

    return response.text