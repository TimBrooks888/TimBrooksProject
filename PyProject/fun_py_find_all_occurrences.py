# fun_py_find_all_occurrences.py
def fun_py_find_all_occurrences(string, substring):
    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        yield start
        start += len(substring)

print(list(fun_py_find_all_occurrences("banana", "na")))
