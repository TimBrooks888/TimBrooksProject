# func_py_generate_happy_numbers.py
def func_py_generate_happy_numbers(limit):
    def is_happy(num):
        seen = set()
        while num != 1 and num not in seen:
            seen.add(num)
            num = sum(int(digit)**2 for digit in str(num))
        return num == 1
    
    return [n for n in range(1, limit) if is_happy(n)]

print(func_py_generate_happy_numbers(100))
