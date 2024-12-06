def print_rect(n, m):
    for _ in range(n):
        print("1" * m)

row_num, col_num = (map(int, input().split()))
print_rect(row_num, col_num)