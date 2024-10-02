a = int(input())
lst = []

for i in range(1,a+1):
    if not(i%2==0 and i%4!=0):
        if not((i//8)%2==0):
            if not((i%7)<4):
                lst.append(i)
print(*lst,sep=" ")