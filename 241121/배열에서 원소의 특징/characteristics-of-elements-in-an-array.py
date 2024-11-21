import sys

N = list(map(int, sys.stdin.readline().split()))
print(next((i for i in range(len(N)) if N[i] % 3 == 0), -1))