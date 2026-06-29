import google.generativeai as genai


def make_image_prompt(product_info):

    prompt = f"""
당신은 대한민국 최고의 쇼핑몰 상세페이지 디자이너입니다.

아래 상품 정보를 이용하여

대표이미지를 AI 이미지 생성 모델이 이해할 수 있도록

영문 프롬프트를 작성하세요.

조건

- White background
- Premium product photography
- Studio lighting
- High quality
- Product centered
- Korean shopping mall style
- Clean composition
- 1000x1000 style

상품정보

{product_info}

영문 프롬프트만 출력하세요.
"""

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    return response.text