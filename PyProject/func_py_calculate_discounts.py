# func_py_calculate_discounts.py
def func_py_calculate_discount(price, discount):
    return price - (price * discount / 100)

print(func_py_calculate_discount(100, 15))
