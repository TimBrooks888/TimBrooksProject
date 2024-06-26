# convert_to_snake_case.py
import re

def to_snake_case(text):
    text = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
    return text

if __name__ == "__main__":
    text = input("Enter a CamelCase text: ")
    snake_case_text = to_snake_case(text)
    print(f"Snake case: {snake_case_text}")
