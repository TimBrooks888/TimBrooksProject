# fun_random_color.py
import random

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

print(random_color())
