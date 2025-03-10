# func_py_caesar_cipher.py
def func_py_caesar_cipher(text, shift=3):
    result = []
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            result.append(char)
    return "".join(result)

print(func_py_caesar_cipher("Hello, World!", 3))
