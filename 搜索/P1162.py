# P1162 填涂颜色
# 深搜

n = int(input())

# 注意：多在外圈包了一层0
matrix = [[0 for _ in range(n+2)] for _ in range(n+2)]

for i in range(1, n+1):
    line = list(map(int, input().split()))
    for j in range(1, n+1):
        matrix[i][j] = line[j-1]


def dfs(i, j):
    if (-1 < i < n + 2) and (-1 < j < n + 2):
        if matrix[i][j] == 0:
            # 标记成外圈0
            matrix[i][j] = 3
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)


dfs(0, 0)

for i in range(1, n+1):
    for j in range(1, n+1):
        if matrix[i][j] == 3:
            print(0, end=' ')
        elif matrix[i][j] == 1:
            print(1, end=' ')
        else:
            print(2, end=' ')
    print()