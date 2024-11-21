import sys
string = sys.stdin.readline().strip()
print(*reversed([string[s] for s in range(len(string)) if s%2==1]),sep="")