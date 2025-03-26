# fun_py_calculate_lcm.py

import math

def fun_py_calculate_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def test_calculate_lcm():
    print(f"LCM of 12 and 18: {fun_py_calculate_lcm(12, 18)}")

if __name__ == "__main__":
    test_calculate_lcm()
