import sys
n = int(sys.stdin.readline())

lst = [sys.stdin.readline().strip() for _ in range(n)]
alpha = sys.stdin.readline().strip()

count = 0
summary = 0

for string in lst:
    if string[0]==alpha:
        count+=1
        summary+=len(string)

print(f"{count} {summary/count:.2f}")