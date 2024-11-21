import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))
count = 0
idx = 0
for i in range(len(lst)):
    if lst[i]==2:
        count+=1
    if count==3:
        idx = i
        break
print(i+1)