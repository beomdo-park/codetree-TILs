n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
s=0
for i in range(n-3):
    for j in range(n-3):
        new_grid = grid[i:i+2][j:j+2]
        count = sum([row.count(1) for row in new_grid])
        s = s if s>count else count
print(s)