# func_calculate_distance.py
def func_calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(func_calculate_distance(0, 0, 3, 4))
