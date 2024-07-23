# fun_py_count_consonants.py
def fun_py_count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in string if char in consonants)

print(fun_py_count_consonants("Hello World"))
