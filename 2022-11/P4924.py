# [1007]魔法少女小Scarlet
# 此处挖坑~貌似Python怎么优化都过不了诶
import numpy as np


n, m = map(int, input().split())

matrix = [[0 for _ in range(n)] for _ in range(n)]
matrix = np.array(matrix)
i = 1
for row in range(n):
    for col in range(n):
        matrix[row][col] = i
        i += 1
# 关于矩阵旋转：
# 当旋转中心为(0,0)时，(i,j)旋转90度变为(j,-i)
# 因此当旋转中心为(x,y)时，可以先考虑平移zhi原点，而后旋转，最终平移回(x,y)处
# 得到如下递推公式：
# 旋转中心为(x,y)，点的坐标为(i,j)，则旋转后的坐标为(j-y+x,x-i+y)


def swap1(x, y, r):
    for i in range(1, r+1):
        # 从内阶逐渐向外旋转
        # 从内阶矩阵的左上角开始，遍历该行即可
        for j in range(2*i):
            t_x = x - i
            t_y = y - i + j
            matrix[t_x][t_y], matrix[x - t_y + y][y + t_x - x], matrix[x - t_x + x][y - t_y + y], matrix[x + t_y - y][y - t_x +
                                                                                                                      x] = matrix[x + t_y - y][y - t_x + x], matrix[t_x][t_y], matrix[x - t_y + y][y + t_x - x], matrix[x - t_x + x][y - t_y + y]


def swap0(x, y, r):
    for i in range(1, r+1):
        # 从内阶逐渐向外旋转
        # 从内阶矩阵的左上角开始，遍历该行即可
        for j in range(2*i):
            t_x = x - i
            t_y = y - i + j
            matrix[t_x][t_y], matrix[t_y - y + x][x + y - t_x], matrix[x - t_x + x][y - t_y + y], matrix[y - t_y + x][y - x +
                                                                                                                      t_x] = matrix[y - t_y + x][y - x + t_x], matrix[t_x][t_y], matrix[t_y - y + x][x + y - t_x], matrix[x - t_x + x][y - t_y + y]


for _ in range(m):
    x, y, r, z = map(int, input().split())
    if z == 0:
        swap0(x-1, y-1, r)
    else:
        swap1(x-1, y-1, r)

for row in matrix:
    for item in row:
        print(item, end=' ')
    print()
print(matrix[1][1])
