import sys

N = list(map(int, sys.stdin.readline().split()))
print(N[next((i-1 for i in range(len(N)) if N[i] % 3 == 0), -1)])