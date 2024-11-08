n = int(input())
lst = list(map(int,input().split()))[::-1]
for i in lst:
    print(f"{i} " if i%2==0 else "",end="")