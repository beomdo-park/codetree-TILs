n = int(input())

num=0
for i in range(n):
    for j in range(n):
        num+=1 if i%2==0 else 2
        print(num,end=" ")
        
    print()