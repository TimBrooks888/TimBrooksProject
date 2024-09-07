# func_py_flatten_nested_list.py
def func_py_flatten_nested_list(lst):
    return [item for sublist in lst for item in sublist]

print(func_py_flatten_nested_list([[1, 2], [3, 4], [5, 6]]))
