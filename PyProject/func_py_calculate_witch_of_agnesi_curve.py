# func_py_calculate_witch_of_agnesi_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_witch_of_agnesi_curve(a, points):
    t = np.linspace(-5, 5, points)
    x = t
    y = 8 * a**3 / (4 * a**2 + t**2)
    plt.plot(x, y)
    plt.title("Witch of Agnesi Curve")
    plt.show()

func_py_calculate_witch_of_agnesi_curve(2, 1000)
