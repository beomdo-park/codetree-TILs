a, b = (map(int,input().split()))

print(sum([num for num in range(a,b+1) if num%6==0 and num%8!=0]))