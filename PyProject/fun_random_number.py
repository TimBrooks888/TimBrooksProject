# fun_random_number.py
import random

def generate_random_number(start, end):
    return random.randint(start, end)

start, end = 1, 100
print(f"Random number between {start} and {end}: {generate_random_number(start, end)}")
