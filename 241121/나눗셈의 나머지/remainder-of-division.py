import sys
from collections import Counter

a,b = map(int,sys.stdin.readline().split())
lst=[]

#다 나누면서 lst append
while a>1:
    몫, 나머지 = divmod(a,b)
    a= 몫
    lst.append(나머지)
    
c = Counter(lst)
sum=0
for i in c.values():
    sum+=i**2
print(sum)