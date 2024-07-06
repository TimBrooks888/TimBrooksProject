# fun_euclidean_distance.py
def euclidean_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

p1 = (1, 2)
p2 = (4, 6)
print(f"Distance between {p1} and {p2}: {euclidean_distance(p1, p2)}")
