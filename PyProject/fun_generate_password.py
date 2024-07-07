# fun_generate_password.py
import random
import string

def fun_generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

print(fun_generate_password())
