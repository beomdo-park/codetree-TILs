import sys
n = int(sys.stdin.readline())

lst = [[1 for _ in range(n)] for _ in range(n)]

for i in range(1, n):
    for j in range(1, n):
        lst[i][j] = lst[i-1][j] + lst[i-1][j-1] + lst[i][j-1]
for row in lst:
    print(" ".join(map(str,row)))