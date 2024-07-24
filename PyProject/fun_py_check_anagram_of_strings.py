# fun_py_check_anagram_of_strings.py
def fun_py_check_anagram_of_strings(str1, str2):
    return sorted(str1) == sorted(str2)

print(fun_py_check_anagram_of_strings("listen", "silent"))
