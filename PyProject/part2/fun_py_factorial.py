# fun_py_factorial.py

def fun_py_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def test_factorial():
    numbers = [5, 7, 10]
    for num in numbers:
        print(f"Factorial of {num}: {fun_py_factorial(num)}")

if __name__ == "__main__":
    test_factorial()
