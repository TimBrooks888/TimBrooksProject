# func_py_is_anagram.py
def func_py_is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print(func_py_is_anagram("listen", "silent"))
