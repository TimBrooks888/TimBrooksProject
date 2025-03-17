# func_py_vowel_count.py

def func_py_vowel_count(text):
    return sum(1 for char in text.lower() if char in "aeiou")

def test_vowel_count():
    words = ["hello", "Python", "umbrella"]
    for word in words:
        print(f"Vowel count in '{word}': {func_py_vowel_count(word)}")

if __name__ == "__main__":
    test_vowel_count()
