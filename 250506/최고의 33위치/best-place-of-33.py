n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
s=0
for i in range(n-2):
    for j in range(n-2):
        new_grid = [row[j:j+3] for row in grid[i:i+3]]
        count = sum([row.count(1) for row in new_grid])
        s = s if s>count else count
print(s)