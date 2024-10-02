flag = 1

for _ in range(5):
    if int(input())%3!=0:
        flag=0
        break
print(flag)