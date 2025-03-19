# func_py_celsius_to_fahrenheit.py

def func_py_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def test_celsius_to_fahrenheit():
    print(f"100°C in Fahrenheit: {func_py_celsius_to_fahrenheit(100)}")

if __name__ == "__main__":
    test_celsius_to_fahrenheit()
