# P3799 妖梦拼木棒
# 4根木棒构成一个正三角形。
# 则必然有两根木棒组成的边等于另外两个木棒组成的边,且另外两个边的长度相等

from math import factorial
n = int(input())

a = [0 for _ in range(5001)]  # 统计每种长度的个数

for _ in range(n):
    i = int(input())
    a[i] += 1

count = 0

if n < 4:
    print(0)
    exit()


def com(n, m):
    return factorial(n)//(factorial(n-m) * factorial(m))


for i in range(5000, 0, -1):
    if a[i] >= 2:
        for j in range(1, i//2 + 1):
            # 好像还是超时~~~开摆！ PyPy3可以过
            if a[j] >= 1 and a[i - j] >= 1 and (i - j) != j:
                t1 = int(com(a[i], 2))
                count += (com(a[i], 2) * com(a[i-j], 1) * com(a[j], 1))
                count %= (10 ** 9 + 7)
            if a[j] >= 2 and (j * 2) == i:
                count += (com(a[i], 2) * com(a[j], 2))
                count %= (10 ** 9 + 7)
            # Python超时，调用math包计算组合数
            # if a[j] >= 1 and a[i - j] >= 1 and (i - j) != j:
            #     count += ((a[i] * (a[i] - 1)) * 0.5 *
            #               a[j] * a[i - j]) % (10 ** 9 + 7)  # Cn2 * Cm1 * Cd1
            # if a[j] >= 2 and (j * 2) == i:
            #     count += ((a[i] * (a[i] - 1)) * 0.5 *
            #               (a[j] * (a[j] - 1)) * 0.5) % (10 ** 9 + 7)  # Cn2 * Cm2
            # count %= (10 ** 9 + 7)
print(int(count))
