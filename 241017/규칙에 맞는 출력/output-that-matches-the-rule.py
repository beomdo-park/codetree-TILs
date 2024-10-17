n = int(input())

for i in range(1, n+1):#열
    for j in range(n-i+1,n+1):
        print(j,end=" ")
    print()