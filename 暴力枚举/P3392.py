# P3392 涂国旗
# 穷举每行变成三种颜色所需的花费

n, m = map(int, input().split())

flag = []  # 读旗帜
for _ in range(n):
    flag.append(input())

res = 999999999999999
for i in range(1, n-1):  # 至少有两行为白色，蓝色
    for j in range(i):  # 至少有一行为蓝色
        count = 0

        # 此时i - j 表示变成白色的行，j表示变成蓝色的行
        temp = 0

        t = 0
        rows = 0
        while t <= j:
            rows += 1
            temp += flag[t].count('W')  # w的数量
            t += 1
        count += (m * rows - temp)  # 全部变成white的次数

        temp = 0
        rows = 0
        while t <= i:
            rows += 1
            temp += flag[t].count('B')  # B的数量
            t += 1
        count += (m * rows - temp)  # 全部变成Bule的次数

        temp = 0
        rows = 0
        while t < n:
            rows += 1
            temp += flag[t].count('R')
            t += 1
        count += (rows * m - temp)
        res = min(count, res)
print(res)
