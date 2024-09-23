# func_py_remove_vowels.py
def func_py_remove_vowels(s):
    return ''.join([char for char in s if char.lower() not in 'aeiou'])

print(func_py_remove_vowels("This is a test sentence"))
