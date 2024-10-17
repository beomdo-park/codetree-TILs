n = int(input())
cnt=9
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(cnt,end="")
        cnt=cnt-1 if cnt>1 else 9
    print()