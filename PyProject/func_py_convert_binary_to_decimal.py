# func_py_convert_binary_to_decimal.py
def func_py_convert_binary_to_decimal(binary_str):
    try:
        return int(binary_str, 2)
    except ValueError:
        return None

print(func_py_convert_binary_to_decimal('1010'))
print(func_py_convert_binary_to_decimal('1001'))
