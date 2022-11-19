# P1045 [NOIP2003 普及组] 麦森数
# 思路
# 判断位数的小技巧：log10（b） + 1  类似于科学计数法
import math
a = int(input())
b = 2 ** a - 1
print(int(math.log10(b) + 1))
# 求最后500位
a = b % (10 ** 500)  # 简化，先求出最后500位
l = []
for i in range(500):
    l.append(a % 10)  # 如果不简化，直接用b的话，会TLE，只有80分
    a = a // 10

for i in range(499, -1, -1):
    print(l[i], end="")
    if i % 50 == 0:
        print("")
