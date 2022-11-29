# P3654 First Step (ファーストステップ)
# 这道题需要注意的是，大于1*K的直线也是可以的~~~
# 先遍历每一行，统计每一行连续'.'等于k的，计算结果。
# 然后在用相同的方法遍历列
# 另外k=1时，行列会重复，因此要/2。

r, c, k = map(int, input().split())

# 读入场地
court = []
for _ in range(r):
    court.append(input())

count = 0  # 统计方案
for i in range(r):
    # 遍历行
    t = 0  # t表示最长的长度
    for j in range(c):
        if court[i][j] == '.':
            t += 1
            # 如果最后一列是'.'，需要额外计算
            if j == c - 1 and t >= k:
                count += t - k + 1
        else:
            if t >= k:
                # 等于k时，只有一种方式
                # 此后每多一个连续的'.'就多一种方式
                count += t - k + 1
            t = 0  # 重置为0

for j in range(c):
    # 遍历列
    t = 0
    for i in range(r):
        if court[i][j] == '.':
            t += 1
            if i == r - 1 and t >= k:
                count += t - k + 1
        else:
            if t >= k:
                # 等于k时，只有一种方式
                # 此后每多一个连续的'.'就多一种方式
                count += t - k + 1
            t = 0  # 重置为0
if k == 1:
    count = count // 2
print(count)
