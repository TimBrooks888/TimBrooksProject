# func_py_calculate_harmonic_mean.py
def func_py_calculate_harmonic_mean(numbers):
    n = len(numbers)
    return n / sum(1 / x for x in numbers)

print(func_py_calculate_harmonic_mean([1, 2, 4]))
