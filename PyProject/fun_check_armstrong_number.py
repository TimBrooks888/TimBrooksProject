# fun_check_armstrong_number.py
def fun_check_armstrong_number(num):
    num_str = str(num)
    num_len = len(num_str)
    return num == sum(int(digit) ** num_len for digit in num_str)

print(fun_check_armstrong_number(153))
print(fun_check_armstrong_number(123))
