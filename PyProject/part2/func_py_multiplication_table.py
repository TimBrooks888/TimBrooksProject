# func_py_multiplication_table.py
def func_py_multiplication_table(n):
    return [[i * j for j in range(1, n+1)] for i in range(1, n+1)]

for row in func_py_multiplication_table(10):
    print(row)
