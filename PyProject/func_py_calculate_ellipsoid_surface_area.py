# func_py_calculate_ellipsoid_surface_area.py
import math

def func_py_calculate_ellipsoid_surface_area(a, b, c):
    p = 1.6075
    return 4 * math.pi * ((a**p * b**p + a**p * c**p + b**p * c**p) / 3)**(1/p)

print(func_py_calculate_ellipsoid_surface_area(3, 4, 5))
