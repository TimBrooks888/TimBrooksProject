# func_py_calculate_lcm.py
import math

def func_py_calculate_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

print(func_py_calculate_lcm(12, 18))
