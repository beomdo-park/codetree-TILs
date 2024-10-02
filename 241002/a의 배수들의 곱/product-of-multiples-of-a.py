from math import prod
a, b = (map(int,input().split()))

print(prod([i for i in range(1, b+1) if i%a==0]))