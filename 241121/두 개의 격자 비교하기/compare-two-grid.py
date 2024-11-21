import sys
n, m = map(int, sys.stdin.readline().split())
lst1 = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
lst2 = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
return_lst = [[1 if lst1[i][j] != lst2[i][j] else 0 for j in range(m)] for i in range(n)]

for row in return_lst:
    print(" ".join(map(str, row)))
