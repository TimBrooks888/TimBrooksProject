# func_find_combinations.py
from itertools import combinations

def func_find_combinations(lst, r):
    return list(combinations(lst, r))

print(func_find_combinations([1, 2, 3, 4], 2))
