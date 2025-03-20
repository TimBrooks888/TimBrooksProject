# func_py_remove_duplicates_from_dict.py

def func_py_remove_duplicates_from_dict(d):
    return {k: v for k, v in d.items() if list(d.values()).count(v) == 1}

def test_remove_duplicates_from_dict():
    data = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
    print(f"Dictionary without duplicates: {func_py_remove_duplicates_from_dict(data)}")

if __name__ == "__main__":
    test_remove_duplicates_from_dict()
