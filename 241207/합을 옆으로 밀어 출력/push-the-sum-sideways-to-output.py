n = int(input())
sum=0
for i in range(n):
    sum+= int(input())
print(str(sum)[1:]+str(sum)[0])