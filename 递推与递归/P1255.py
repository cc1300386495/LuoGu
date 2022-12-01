# P1255 数楼梯
# 因为每步可以走1-2阶，所以如果想要走到n阶，就得从n-1阶或者n-2阶开始走
# 如果我们知道了走到n-2阶或者n-1阶可能的方法，相加即可得到走到n阶的方法数。

# 复杂度 O(2^n)
# def f(n):
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2  # 有两种方法，走两步1阶，或者一步2阶
#     else:
#         return f(n-1) + f(n-2)


n = int(input())
dp = [0 for _ in range(50001)]
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
