# func_py_find_prime_factors.py
def func_py_find_prime_factors(n):
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while (n % divisor) == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return factors
