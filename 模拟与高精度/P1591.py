# P1591 阶乘数码
# 模拟即可
from math import factorial
t = int(input())


def calc(n, a):
    res = factorial(n)
    cnt = 0
    while res:
        if res % 10 == a:  # 取结果的每一位进行比较
            cnt += 1
        res = res // 10
    return cnt


for _ in range(t):
    n, a = map(int, input().split())
    print(calc(n, a))
