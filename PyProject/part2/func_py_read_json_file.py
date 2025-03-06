# func_py_read_json_file.py
import json

def func_py_read_json_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

print(func_py_read_json_file("data.json"))
