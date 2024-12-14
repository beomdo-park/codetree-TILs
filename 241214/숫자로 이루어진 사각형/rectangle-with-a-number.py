N=int(input())
num=0
def rectengle(N):
    global num
    for i in range(N):
        for j in range(N):
            print(f"{num%9+1}",end=" ")
            num+=1
        print()
rectengle(N)