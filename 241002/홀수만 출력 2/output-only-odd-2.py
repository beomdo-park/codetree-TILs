b, a = (map(int,input().split()))

print(*[i for i in range(b,a-1,-1) if i%2==1])