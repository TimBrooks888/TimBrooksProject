# func_py_calculate_regular_pyramid_surface_area.py
import math

def func_py_calculate_regular_pyramid_surface_area(base_perimeter, base_area, slant_height):
    lateral_area = (base_perimeter * slant_height) / 2
    return base_area + lateral_area

print(func_py_calculate_regular_pyramid_surface_area(24, 30, 10))
