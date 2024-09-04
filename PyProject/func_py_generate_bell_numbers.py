# func_py_generate_bell_numbers.py
def func_py_generate_bell_numbers(n):
    bell = [[0 for _ in range(n)] for _ in range(n)]
    bell[0][0] = 1
    for i in range(1, n):
        bell[i][0] = bell[i - 1][-1]
        for j in range(1, i + 1):
            bell[i][j] = bell[i][j - 1] + bell[i - 1][j - 1]
    return [bell[i][i] for i in range(n)]

print(func_py_generate_bell_numbers(5))
