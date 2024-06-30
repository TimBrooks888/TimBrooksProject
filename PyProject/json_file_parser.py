# json_file_parser.py
import json

def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    filename = input("Enter the JSON file name: ")
    try:
        data = read_json(filename)
        print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
``
