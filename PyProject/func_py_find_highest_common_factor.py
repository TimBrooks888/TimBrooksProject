# func_py_find_highest_common_factor.py
def func_py_find_highest_common_factor(a, b):
    while b:
        a, b = b, a % b
    return a

print(func_py_find_highest_common_factor(48, 18))
