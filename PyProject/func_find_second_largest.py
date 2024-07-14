# func_find_second_largest.py
def func_find_second_largest(lst):
    sorted_lst = sorted(set(lst), reverse=True)
    return sorted_lst[1] if len(sorted_lst) > 1 else None

print(func_find_second_largest([1, 2, 3, 4, 5]))
