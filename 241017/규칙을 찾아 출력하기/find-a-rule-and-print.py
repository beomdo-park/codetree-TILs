n = int(input())

#4기준
if n==1:
    print('*')
else:
    print('* '*n)
    for i in range(n-2,0,-1):
        print('* '*(n-i-1)+'  '*i+'* ')
    print('* '*n)