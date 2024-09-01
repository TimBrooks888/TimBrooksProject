# func_py_calculate_superellipse_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_superellipse_curve(a, b, n, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = np.sign(np.cos(t)) * (np.abs(np.cos(t)))**(2/n) * a
    y = np.sign(np.sin(t)) * (np.abs(np.sin(t)))**(2/n) * b
    plt.plot(x, y)
    plt.title("Superellipse Curve")
    plt.show()

func_py_calculate_superellipse_curve(5, 3, 4, 1000)
