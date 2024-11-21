import sys
lst = []

for i in range(4):
    lst.append(list(map(int, sys.stdin.readline().split())))

sum=0
for i in range(len(lst)):
    for j in range(i+1):
        sum+=lst[i][j]
print(sum)