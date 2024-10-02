cnt = 0
for _ in range(5):
    cnt=cnt+1 if int(input())%2==0 else cnt
print(cnt)