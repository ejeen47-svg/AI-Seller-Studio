def calculate_price(
    china_price,
    exchange_rate,
    international_shipping,
    domestic_shipping,
    margin_rate
):

    product_cost = china_price * exchange_rate

    total_cost = (
        product_cost
        + international_shipping
        + domestic_shipping
    )

    selling_price = total_cost * (1 + margin_rate / 100)

    return {
        "원가": round(product_cost),
        "총원가": round(total_cost),
        "권장판매가": round(selling_price),
        "예상마진": round(selling_price - total_cost)
    }