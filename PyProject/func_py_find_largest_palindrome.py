# func_py_find_largest_palindrome.py
def func_py_find_largest_palindrome(lst):
    palindromes = [num for num in lst if str(num) == str(num)[::-1]]
    return max(palindromes) if palindromes else None

print(func_py_find_largest_palindrome([121, 232, 454, 789]))
