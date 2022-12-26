# P1024 [NOIP2001 提高组] 一元三次方程求解
# 枚举写法

a = list(map(float, input().split()))


def f(x): return a[0] * x ** 3 + a[1] * x ** 2 + a[2] * x ** 1 + a[3]


res = 0
i = - 100
while i <= 100:
    if f(i) * f(i+0.01) < 0:
        print("%.2f" % i, end=" ")
        res += 1
    if res == 3:
        break
    i += 0.01
