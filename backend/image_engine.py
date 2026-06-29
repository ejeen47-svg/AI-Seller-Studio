import google.generativeai as genai


def generate_image_prompt(product_info):

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
너는 대한민국 최고의 쇼핑몰 디자이너다.

아래 상품정보를 보고

스마트스토어와 쿠팡에서 클릭률이 높은

1000x1000 대표이미지를 만들기 위한 프롬프트를 작성해라.

조건

- 흰색 배경
- 제품만 크게
- 글자 없음
- 로고 없음
- 쇼핑몰 대표이미지
- 고급스럽게
- 사실적인 사진
- 그림체 금지

상품정보

{product_info}

프롬프트만 출력.
"""

    response = model.generate_content(prompt)

    return response.text