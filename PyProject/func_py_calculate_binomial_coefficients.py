# func_py_calculate_binomial_coefficients.py
def func_py_calculate_binomial_coefficients(n, k):
    if k == 0 or k == n:
        return 1
    return func_py_calculate_binomial_coefficients(n - 1, k - 1) + func_py_calculate_binomial_coefficients(n - 1, k)

print(func_py_calculate_binomial_coefficients(5, 2))
