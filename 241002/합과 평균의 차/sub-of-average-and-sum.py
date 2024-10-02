import sys

a,b,c = (map(int,sys.stdin.readline().split()))

print(a+b+c)
print((a+b+c)//3)
print((a+b+c)-(a+b+c)//3)