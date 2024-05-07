def calculate_price(base_price: int, consumption_tax: float) -> float:
    sales_price = base_price * (1 + consumption_tax)
    return sales_price

print(calculate_price(500, 0.1))
