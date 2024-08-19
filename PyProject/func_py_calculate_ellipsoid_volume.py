# func_py_calculate_ellipsoid_volume.py
import math

def func_py_calculate_ellipsoid_volume(a, b, c):
    return (4/3) * math.pi * a * b * c

print(func_py_calculate_ellipsoid_volume(3, 4, 5))
