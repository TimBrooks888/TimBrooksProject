# fun_py_get_unique_elements.py

def fun_py_get_unique_elements(lst):
    return list(set(lst))

def test_get_unique_elements():
    numbers = [1, 2, 2, 3, 4, 4, 5]
    print(f"Unique elements: {fun_py_get_unique_elements(numbers)}")

if __name__ == "__main__":
    test_get_unique_elements()
