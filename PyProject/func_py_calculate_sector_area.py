# func_py_calculate_sector_area.py
import math

def func_py_calculate_sector_area(radius, angle):
    return (angle / 360) * math.pi * radius**2

print(func_py_calculate_sector_area(5, 90))
