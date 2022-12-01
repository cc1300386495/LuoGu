# P1028 [NOIP2001 普及组] 数的计算
# 维护一个dp数组，dp[i]表示n为i时，可以组成的合法数量

n = int(input())
dp = [0 for _ in range(1001)]
# 转移方程：
# 题目要求，要接的数必须小于末尾，那么假如我们要给n后面接一些数
# 那么只能从1~n//2中选，而dp[1]~dp[n//2]，在遍历到n时是已知的，由此得到了
# dp[n] = dp[1] + ······ + dp[n//2]

# 超时
# count = 1
# def dfs(n):
#     global count
#     if n == 1:
#         return
#     else:
#         for i in range(1, n//2+1):
#             count += 1
#             dfs(i)

for i in range(1, n+1):
    dp[i] += 1  # 它本身
    for j in range(1, i//2+1):
        dp[i] += dp[j]
print(dp[n])
