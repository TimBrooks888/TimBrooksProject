# func_py_find_largest_even.py
def func_py_find_largest_even(lst):
    evens = [num for num in lst if num % 2 == 0]
    return max(evens) if evens else None

print(func_py_find_largest_even([1, 2, 3, 4, 5, 6]))
