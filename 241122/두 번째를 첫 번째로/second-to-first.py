A = input()
fst = A[0]
snd = A[1]
for i in range(len(A)):
    print(A[i],end="") if A[i]!=snd else print(fst,end="")