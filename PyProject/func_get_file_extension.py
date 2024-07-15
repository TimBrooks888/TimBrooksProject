# func_get_file_extension.py
def func_get_file_extension(filename):
    return filename.split('.')[-1] if '.' in filename else ''

print(func_get_file_extension("example.txt"))
