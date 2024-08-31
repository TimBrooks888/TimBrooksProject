# func_py_generate_pell_numbers.py
def func_py_generate_pell_numbers(limit):
    pell_numbers = [0, 1]
    for i in range(2, limit):
        pell_numbers.append(2 * pell_numbers[-1] + pell_numbers[-2])
    return pell_numbers

print(func_py_generate_pell_numbers(10))
