import re

def extract_section(text, title):
    """
    ### 제목
    내용
    형태의 텍스트에서 제목에 해당하는 내용만 추출
    """

    pattern = rf"###\s*{re.escape(title)}\s*(.*?)(?=\n###|\Z)"

    match = re.search(pattern, text, re.S)

    if match:
        return match.group(1).strip()

    return ""


def parse_result(text):

    return {
        "smartstore_title": extract_section(text, "스마트스토어 상품명"),
        "coupang_title": extract_section(text, "쿠팡 상품명"),
        "tags": extract_section(text, "태그"),
        "color": extract_section(text, "색상"),
        "option": extract_section(text, "옵션"),
        "size": extract_section(text, "사이즈"),
        "material": extract_section(text, "재질"),
        "components": extract_section(text, "구성품"),
        "features": extract_section(text, "상품특징"),
        "description": extract_section(text, "상품설명"),
    }