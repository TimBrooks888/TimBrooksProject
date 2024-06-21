# circle_area_calculator.py
import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

radius = 5
area = calculate_circle_area(radius)
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
