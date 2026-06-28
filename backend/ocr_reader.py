import google.generativeai as genai


def read_chinese(images):

    prompt = """
업로드된 이미지 속의 모든 중국어를 읽어주세요.

번역하지 말고

중국어 원문만 순서대로 출력하세요.

광고문구도 모두 읽으세요.

표도 읽으세요.

사이즈도 읽으세요.

텍스트를 빠짐없이 출력하세요.
"""

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    response = model.generate_content(
        [prompt] + images
    )

    return response.text