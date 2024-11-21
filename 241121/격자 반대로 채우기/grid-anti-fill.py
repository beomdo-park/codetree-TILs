import sys

n = int(sys.stdin.readline())
matrix = [[n * i + j + 1 for j in range(n)] for i in range(n)]

#짝수 줄 역순만들기
for i in range(1, n):
    if i%2==1:
        matrix[i]=matrix[i][::-1]

result_matrix = [[0 for i in range(n)] for j in range(n)]
#행 열 바꿔주기
for i in range(n):
    for j in range(n):
        result_matrix[i][j] = matrix[n-j-1][n-i-1]

for row in result_matrix:
    print(" ".join(map(str,row)))