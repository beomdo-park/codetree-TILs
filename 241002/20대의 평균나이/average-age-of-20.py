from functools import reduce
sum=0
cnt = 0
while True:
    n = int(input())
    
    if n//10==2:
        sum+=n
        cnt+=1
    else:
        break
print("%.2f" %(sum/cnt))