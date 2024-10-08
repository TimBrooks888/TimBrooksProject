# func_py_count_vowels_and_consonants.py
def func_py_count_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = consonant_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count
