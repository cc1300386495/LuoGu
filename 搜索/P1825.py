# P1825 [USACO11OPEN]Corn Maze S
# bfs典型题

n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(input())

# 记录到达每个点的步数
step = [[99999999 for _ in range(m)] for _ in range(n)]
# 判断有没有走过这个位置
vis = [[1 for _ in range(m)] for _ in range(n)]
# 传送门
door = {}
for i in range(n):
    for j in range(m):
        # 找起点
        if matrix[i][j] == '@':
            startX, startY = i, j
        # 找终点
        if matrix[i][j] == '=':
            endX, endY = i, j
        # 找传送门
        if 'A' <= matrix[i][j] <= 'Z':
            if door.get(matrix[i][j], 0) == 0:
                door[matrix[i][j]] = [[i, j]]
            else:
                temp = door[matrix[i][j]]
                temp.append([i, j])
                door[matrix[i][j]] = temp

# 开始宽搜
q = []
q.append([startX, startY])
step[startX][startY] = 0
vis[startX][startY] = 0
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

while q:
    x, y = q.pop(0)
    if x == endX and y == endY:
        break
    for moveX, moveY in direction:
        # 如果没越界
        if -1 < x + moveX < n and -1 < y + moveY < m and matrix[x+moveX][y+moveY] != '#':
            # 如果没走过
            if vis[x+moveX][y + moveY]:
                # 再判断是不是传送门
                if 'A' <= matrix[x+moveX][y+moveY] <= 'Z':
                    # 如果是传送门
                    for toX, toY in door[matrix[x+moveX][y+moveY]]:
                        # 找到了传送门的目的地
                        if (toX != x+moveX) or (toY != y + moveY):
                            step[toX][toY] = min(
                                step[toX][toY], step[x][y] + 1)
                            q.append([toX, toY])

                else:
                    vis[x+moveX][y+moveY] = 0
                    step[x+moveX][y +
                                  moveY] = min(step[x+moveX][y + moveY], step[x][y] + 1)
                    q.append([x+moveX, y+moveY])

print(step[endX][endY])
