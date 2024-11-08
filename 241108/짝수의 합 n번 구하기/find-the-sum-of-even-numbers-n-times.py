n = int(input())

for _ in range(n):
    sum=0
    a,b = (map(int,input().split()))
    for i in range(a,b+1):
        sum+=i if i%2==0 else 0
    print(sum)