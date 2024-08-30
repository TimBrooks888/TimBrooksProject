# func_py_generate_harmonic_numbers.py
def func_py_generate_harmonic_numbers(limit):
    harmonic_numbers = [1]
    for n in range(2, limit + 1):
        harmonic_numbers.append(harmonic_numbers[-1] + 1/n)
    return harmonic_numbers

print(func_py_generate_harmonic_numbers(10))
