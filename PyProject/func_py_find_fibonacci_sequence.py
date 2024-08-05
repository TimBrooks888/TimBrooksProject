# func_py_find_fibonacci_sequence.py
def func_py_find_fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(func_py_find_fibonacci_sequence(10))
