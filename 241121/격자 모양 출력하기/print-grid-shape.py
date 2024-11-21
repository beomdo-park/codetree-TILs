import sys
n, m = (map(int,sys.stdin.readline().split()))

matrix = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    row, col = (map(int,sys.stdin.readline().split()))
    matrix[row-1][col-1] = row*col

for row in matrix:
    print(" ".join(map(str,row)))    
