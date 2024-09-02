# func_py_calculate_ellipse_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_ellipse_curve(a, b, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = a * np.cos(t)
    y = b * np.sin(t)
    plt.plot(x, y)
    plt.title("Ellipse Curve")
    plt.show()

func_py_calculate_ellipse_curve(5, 3, 1000)
