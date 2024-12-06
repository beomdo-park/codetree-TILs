A = input()
B = input()

cnt=0
while True:
    A = A[-1]+A[:-1]
    cnt+=1
    if A==B:
        print(cnt)
        break
    elif cnt==len(A)+1:
        print(-1)
        break