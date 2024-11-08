N = int(input())

n = 65
for i in range(N):
    for j in range(N-i):
        print(chr(n),end=" ")
        n+=1
    print()
    print("  "*(N-j),end="")