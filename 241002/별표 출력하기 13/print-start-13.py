high_num = int(input())
low_num = 1


for i in range(high_num):
    print('* '*(high_num-i))
    print('* '*(low_num+i))