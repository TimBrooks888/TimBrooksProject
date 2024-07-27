# func_py_generate_palindrome_numbers.py
def func_py_generate_palindrome_numbers(n):
    palindrome_numbers = []
    for num in range(1, n+1):
        if str(num) == str(num)[::-1]:
            palindrome_numbers.append(num)
    return palindrome_numbers

print(func_py_generate_palindrome_numbers(100))
