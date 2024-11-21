import sys
lst = [sys.stdin.readline().strip() for _ in range(3)]
lst.sort(key=len)
print(len(lst[-1])-len(lst[0]))