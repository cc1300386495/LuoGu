# P1596 [USACO10OCT]Lake Counting S
# 这次用宽搜~~~
from collections import deque
n, m = map(int, input().split())

matrix = [['' for _ in range(m)]for _ in range(n)]
vis = [[0 for _ in range(m)]for _ in range(n)]
for i in range(n):
    line = input()
    for j in range(m):
        matrix[i][j] = line[j]

count = 0
# 八个搜索方向
direction = [[1, 0], [-1, -1], [0, -1],
             [1, -1], [-1, 0], [1, 1], [0, 1], [-1, 1]]

for i in range(n):
    for j in range(m):
        # 如果它是水，就开始宽搜，把它连着的水都变成陆地
        if matrix[i][j] == 'W' and vis[i][j] == 0:
            que = deque([[i, j]])
            vis[i][j] = 1
            while que:
                x, y = que.popleft()
                # 向八个方向搜索
                for move_x, move_y in direction:
                    if (-1 < x + move_x < n) and (-1 < y + move_y < m):
                        # 说明没越界
                        if matrix[x + move_x][y + move_y] == 'W' and vis[x + move_x][y + move_y] == 0:
                            vis[x + move_x][y + move_y] = 1
                            que.append([x + move_x, y + move_y])
            count += 1
print(count)
