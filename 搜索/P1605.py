# P1605 迷宫
# 深度搜索模板题

N, M, T = map(int, input().split())

matrix = [[0 for i in range(M)]for i in range(N)]
sx, sy, fx, fy = map(int, input().split())
sx, sy, fx, fy = sx-1, sy-1, fx-1, fy-1
# 记录障碍
for i in range(T):
    x, y = map(int, input().split())
    matrix[x-1][y-1] = 1


res = 0

move = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs(x, y):
    global res, matrix
    if (x == fx) and (y == fy):
        res += 1
        return
    for move_x, move_y in move:
        if -1 < x + move_x < N and -1 < y + move_y < M and matrix[x+move_x][y+move_y] == 0:
            matrix[x+move_x][y+move_y] = 1
            dfs(x+move_x, y+move_y)
            matrix[x+move_x][y+move_y] = 0

matrix[sx][sy] = 1
dfs(sx, sy)
print(res)
