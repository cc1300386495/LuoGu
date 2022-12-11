# P1990 覆盖墙壁
#  动态规划

n = int(input())
mod = 10000
# d[N] 表示铺满前N*2的面积的墙的方案数
# g[N]来表示**铺满前(N+1)*2的面积的墙，但是第(N+1)列有一个瓷砖已经被铺过
d = [0 for _ in range(n+10)]
g = [0 for _ in range(n+10)]

# 初始化
d[0] = 1
g[0] = 0
g[1] = 1
d[1] = 1

# 递推公式：
# d[N]=d[N-1]+d[N-2]+2*g[N-2]
# g[N]=d[N-1]+g[N-1]

for i in range(2, n+1):
    d[i] = ((d[i-1]+d[i-2]) % mod+2*g[i-2] % mod) % mod
    g[i] = (g[i-1]+d[i-1]) % mod

print(d[n])
