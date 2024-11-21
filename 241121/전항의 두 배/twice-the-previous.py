import sys

lst = list(map(int, sys.stdin.readline().split()))
# A3 = 2*A1 + A2

for i in range(2,10):
    lst.append(2*lst[i-2]+lst[i-1])
print(*lst)