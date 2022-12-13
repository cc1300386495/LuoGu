# P1498 南蛮图腾
# 构建图腾的方法就是
# 将大小为n-1的图腾向右复制一个，在向上加一个，即可德奥大小为n的图腾

# 存储图腾
pic = [[' ' for _ in range(3000)] for _ in range(3000)]

# n = 1 时的长和宽
height = 2
weight = 4
# 先构造n = 1时的图腾
pic[1][2] = '/'
pic[2][1] = '/'
pic[1][3] = '\\'
pic[2][4] = '\\'
pic[2][2] = '_'
pic[2][3] = '_'

n = int(input())

for i in range(1, n):
    # 向下平移后向右复制
    for h in range(1, height+1):
        for j in range(1, weight+1):
            # 向下平移
            pic[h+height][j] = pic[h][j]
            # 向右复制
            pic[h+height][j+weight] = pic[h][j]
            pic[h][j] = ' '  # 原来的地方清空
    # 补上方的图腾
    for h in range(1, height+1):
        for j in range(1, weight+1):
            pic[h][j+weight//2] = pic[h+height][j]
    # 规模扩大两倍
    height *= 2
    weight *= 2
 # 打印结果
for i in range(1, height+1):
    for j in range(1, weight+1):
        print(pic[i][j], end='')
    print()
