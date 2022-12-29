# P1433 吃奶酪
# 状态压缩 + 动态规划

# 状态压缩是指将某种状态利用二进制表示出来
# 在本题中就表示N个点用长度为N的二进制表示，如果第i点走过，则第i位为1

N = int(input())
# 存储每个点的x坐标
x = [0 for i in range(20)]
# 存储每个点的y坐标
y = [0 for i in range(20)]

# 读取坐标
for i in range(1, N+1):
    x[i], y[i] = map(float, input().split())


def dis(i, j):
    return ((x[i]-x[j]) ** 2 + (y[i]-y[j]) ** 2) ** 0.5


# 初始化每个点之间的距离
a = [[0 for i in range(N+1)] for i in range(N+1)]
for i in range(N+1):
    for j in range(i+1, N+1):
        a[i][j] = dis(i, j)
        a[j][i] = a[i][j]


# 初始化f数组
# f[i][k]表示在i点时，状态为k的最短距离
# 举例说明状态的含义:
# 假如有三个点，如果每个点都没走过，那么就是k就是000对应的十进制也就是0
# 如果所有点都走过，那么k就是111对应的十进制也就是7
# 初始化f数组就是从原点到达每个点的距离
# 开大一点
f = [[99999999 for i in range(50000)] for i in range(30)]
for i in range(1, N+1):
    # 1 << (i-1) 就表示只到达过i点的状态
    f[i][(1 << (i-1))] = a[0][i]


# 三重循环更新f数组
# 先枚举所有的状态
for k in range(1, 1 << N):
    # 再枚举每个点
    for i in range(1, N+1):
        # 如果这个点在当前状态里没来过，那么显然是矛盾的，所有略过
        if (k & (1 << (i-1))) == 0:
            continue
        # 枚举更新其他点到i点的距离
        for j in range(1, N+1):
            if i == j:
                # 相同的点不需要更新
                continue
            if (k & (1 << (j-1))) == 0:
                continue
            # 比较从j点到i点的距离会不会更短
            f[i][k] = min(f[i][k], f[j][k - (1 << (i-1))] + a[i][j])

# 寻找答案
ans = 9999999
for i in range(1, N+1):
    ans = min(ans, f[i][(1 << N)-1])

print("%.2f" % ans)
