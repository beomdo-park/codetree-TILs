import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

min_diff = 100000
for i in range(1,len(lst)):
    for j in range(i,len(lst)):
        diff =abs(lst[j]-lst[i-1])
        if diff<min_diff:
            min_diff=diff
print(min_diff)