# P2437 蜜蜂路线
# 与P1255雷同

m, n = map(int, input().split())

# 做变换，m变成1
n = n - m + 1
m = 1

# 开一个dp数组
dp = [0 for i in range(n+10)]
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])
