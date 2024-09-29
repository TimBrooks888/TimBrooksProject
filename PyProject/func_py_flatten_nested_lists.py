def func_py_flatten_nested_list(nested_list):
    result = []
    for i in nested_list:
        if isinstance(i, list):
            result.extend(func_py_flatten_nested_list(i))
        else:
            result.append(i)
    return result
