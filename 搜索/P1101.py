# P1101 单词方阵
# n皇后的既视感。。。。
# 先构建一个n*n的bool矩阵，全部设置为True
# 然后深搜，如果某个位置是yizhong的一部分就设置为False
# 最后输出即可

n = int(input())

judge = [[True for _ in range(n)] for _ in range(n)]

# 读数据
matrix = [['' for _ in range(n)]for _ in range(n)]
for i in range(n):
    line = input()
    for j in range(n):
        matrix[i][j] = line[j]

s = 'yizhong'

# 记录能连成yizhong的下标
record = []

# 记录八个搜索方向的x,y变化
direction = [[1, 0], [-1, -1], [0, -1],
             [1, -1], [-1, 0], [1, 1], [0, 1], [-1, 1]]


def dfs(x, y, d, loc):
    global record, judge
    # x,y表示坐标
    # d 表示搜索方向
    # loc表示搜索yizhong的第几个字母

    # 越界返回
    if x < 0:
        return
    if y < 0:
        return
    if x >= n:
        return
    if y >= n:
        return
    # 不符合要求
    if matrix[x][y] != s[loc]:
        return
    # 说明此时此刻连成了yizhong
    if loc == 6 and matrix[x][y] == 'g':
      # 更新judge数组
        for n_x, n_y in record:
            judge[n_x][n_y] = False
        judge[x][y] = False
        return

    # 如果走到这还没有return，说明就得继续深搜
    change_x, change_y = direction[d]
    record.append([x, y])
    dfs(x+change_x, y+change_y, d, loc+1)
    record.pop()


for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'y':
            for t in range(8):
                # 沿八个方向搜索
                dfs(i, j, t, 0)

# 输出答案
for i in range(n):
    for j in range(n):
        if judge[i][j]:
            print('*', end='')
        else:
            print(matrix[i][j], end='')
    print()
