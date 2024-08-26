# func_py_generate_strobogrammatic_numbers.py
def func_py_generate_strobogrammatic_numbers(limit):
    strobogrammatic_pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    
    def is_strobogrammatic(num):
        return all(str(digit) in strobogrammatic_pairs and strobogrammatic_pairs[str(digit)] == str(rev_digit)
                   for digit, rev_digit in zip(str(num), str(num)[::-1]))
    
    return [n for n in range(1, limit) if is_strobogrammatic(n)]

print(func_py_generate_strobogrammatic_numbers(1000))
