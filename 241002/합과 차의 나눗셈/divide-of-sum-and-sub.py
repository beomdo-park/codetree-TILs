import sys

a,b = (map(int, sys.stdin.readline().split()))

print("%.2f"%((a+b)/(a-b)))