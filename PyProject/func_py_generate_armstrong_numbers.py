# func_py_generate_armstrong_numbers.py
def fun_py_generate_armstrong_numbers(n):
    armstrong_numbers = []
    for num in range(n+1):
        num_str = str(num)
        length = len(num_str)
        sum_of_powers = sum(int(digit) ** length for digit in num_str)
        if num == sum_of_powers:
            armstrong_numbers.append(num)
    return armstrong_numbers

print(fun_py_generate_armstrong_numbers(1000))
