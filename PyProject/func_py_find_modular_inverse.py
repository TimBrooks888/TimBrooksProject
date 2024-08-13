# func_py_find_modular_inverse.py
def func_py_find_modular_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

print(func_py_find_modular_inverse(3, 11))
