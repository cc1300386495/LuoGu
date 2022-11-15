# P1009 [NOIP1998 普及组] 阶乘之和
n = int(input())


def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)


def cal(n):
    if n == 1:
        return 1
    else:
        return fac(n) + cal(n-1)


print(cal(n))
