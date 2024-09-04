# func_py_calculate_von_koch_curve.py
import matplotlib.pyplot as plt

def func_py_calculate_von_koch_curve(iterations):
    def koch_curve(p1, p2, iteration):
        if iteration == 0:
            return [p1, p2]
        delta_x, delta_y = (p2[0] - p1[0]) / 3, (p2[1] - p1[1]) / 3
        p3 = (p1[0] + delta_x, p1[1] + delta_y)
        p4 = (p1[0] + 2 * delta_x, p1[1] + 2 * delta_y)
        p5 = (p3[0] + delta_x * 0.5 - delta_y * np.sqrt(3) / 2, p3[1] + delta_y * 0.5 + delta_x * np.sqrt(3) / 2)
        return koch_curve(p1, p3, iteration - 1) + koch_curve(p3, p5, iteration - 1) + koch_curve(p5, p4, iteration - 1) + koch_curve(p4, p2, iteration - 1)

    curve = koch_curve((0, 0), (1, 0), iterations)
    plt.plot(*zip(*curve))
    plt.title("Von Koch Curve")
    plt.show()

func_py_calculate_von_koch_curve(4)
