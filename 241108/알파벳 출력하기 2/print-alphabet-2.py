N = int(input())

n = 65
for i in range(N):
    for j in range(N-i):
        print(chr(n),end=" ")
        n=n+1 if n<90 else 65
    print()
    print("  "*(N-j),end="")