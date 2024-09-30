# func_py_find_median.py
def func_py_find_median(lst):
    sorted_lst = sorted(lst)
    length = len(lst)
    if length % 2 == 0:
        return (sorted_lst[length // 2 - 1] + sorted_lst[length // 2]) / 2
    else:
        return sorted_lst[length // 2]
