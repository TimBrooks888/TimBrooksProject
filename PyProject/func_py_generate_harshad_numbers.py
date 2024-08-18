# func_py_generate_harshad_numbers.py
def func_py_generate_harshad_numbers(limit):
    return [i for i in range(1, limit + 1) if i % sum(int(digit) for digit in str(i)) == 0]

print(func_py_generate_harshad_numbers(100))
