a, n = map(int,input().split())

print(*[a+n*i for i in range(1,n+1)],sep="\n")