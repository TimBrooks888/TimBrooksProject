# count_even_odd.py
def count_even_odd(lst):
    even_count = sum(1 for x in lst if x % 2 == 0)
    odd_count = len(lst) - even_count
    return even_count, odd_count

if __name__ == "__main__":
    lst = list(map(int, input("Enter numbers separated by space: ").split()))
    even_count, odd_count = count_even_odd(lst)
    print(f"Even numbers: {even_count}, Odd numbers: {odd_count}")
