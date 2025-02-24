# 8. 找到列表中出现次数最多的元素
def most_frequent(lst):
    return max(set(lst), key=lst.count)

print(most_frequent([1, 3, 3, 2, 1, 3, 4, 3, 2]))  # 3
