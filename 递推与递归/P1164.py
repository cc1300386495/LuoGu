# P1164 小A点菜
# 类似于背包问题
# 构造dp数组

# 读入数据
N, M = map(int, input().split())
# 部分数据不是一行给出的
price = [0] * (N + 10)
index = 1
while True:
    l = list(map(int, input().split()))
    for item in l:
        price[index] = item
        index += 1
    if N < index:
        break
# dp[i][j]表示前i种菜品，恰好花费j元的种类数
dp = [[0 for _ in range(M + 10)] for _ in range(N+10)]

for i in range(1, N+1):
    for j in range(1, M + 1):
        if j < price[i]:
            dp[i][j] = dp[i-1][j]
        if j == price[i]:
            dp[i][j] = dp[i-1][j] + 1
        if j > price[i]:
            dp[i][j] = dp[i-1][j] + dp[i-1][j - price[i]]

print(dp[N][M])
