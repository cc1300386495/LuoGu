# P2241 统计方形（数据加强版）
# 数学题
# 正方形个数：
# 边长为1的正方形个数： n*m
# 边长为2的正方形个数：(n-1) * (m-1)
# ·······
# 边长最长为min{n,m}，个数为：(n-min{n,m}+1) * (m-min{n,m}+1)
# 矩阵个数 = 正方形个数 + 长方形个数
# 矩形个数 = (1+2+3+···+n)*(1+2+3+···+m)
# 从而间接推出长方形个数

n, m = map(int, input().split())

s1 = 0
for i in range(1, min(n, m)+1):
    s1 += (n-i+1)*(m-i+1)

s2 = sum([i for i in range(n+1)]) * sum([j for j in range(m+1)])

print(s1, s2-s1, sep=' ')
