# func_generate_multiplication_table.py
def func_generate_multiplication_table(n):
    table = []
    for i in range(1, n+1):
        row = [i * j for j in range(1, n+1)]
        table.append(row)
    return table

for row in func_generate_multiplication_table(5):
    print(row)
