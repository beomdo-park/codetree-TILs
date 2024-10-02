n = int(input())
cnt=0
while n<1000:
    n=n*3+1 if n%2==0 else n*2+2 
    cnt+=1
print(cnt)