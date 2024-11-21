import sys

lst = [sys.stdin.readline().strip().replace(" ", "") for _ in range(2)]
print("".join(lst))