# func_py_find_lcm.py
import math

def func_py_find_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

print(func_py_find_lcm(54, 24))
