# func_py_median_of_list.py

def func_py_median_of_list(lst):
    sorted_lst = sorted(lst)
    mid = len(sorted_lst) // 2
    return (sorted_lst[mid] + sorted_lst[mid - 1]) / 2 if len(lst) % 2 == 0 else sorted_lst[mid]

def test_median_of_list():
    lists = [[1, 3, 3, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6], [7, 8, 9, 10]]
    for lst in lists:
        print(f"Median of {lst}: {func_py_median_of_list(lst)}")

if __name__ == "__main__":
    test_median_of_list()
