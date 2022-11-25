# P1088 [NOIP2004 普及组] 火星人
# 题意是将全排列从大到小映射成从1开始的连续整数
# 然后加上一个小的数字后，再反向映射出全排列，然后输出。

# n的范围比较大，会TLE。因此这里引入 康托展开
# 康托展开 也是用于完成 全排列到自然数的双射

# 详细介绍请看该目录下的 康托展开.md
# 代码实现 注意：该算法对于Python仍然会超时，只有80分。

# 可通过类似的思想，从最后一位往后加，直至加了m个。
# 满分代码见末尾


# 求阶乘 后续计算会用
import math


n = int(input())
m = int(input())
r = list(map(int, input().split()))


tag = [0 for _ in range(n+1)]  # 用于标记数有没有出现过
tag[0] = 1  # 0不考虑

# 求出r对应的康托展开
order = 0  # 对应的康托展开
for i in range(n):
    item = r[i]  # 取所给组合的第i+1位
    t = 0  # 遍历所有小于item的数
    cnt = 0  # 统计未出现且小于item的数的个数
    while t < item:
        if not tag[t]:
            cnt += 1
        t += 1
    tag[item] = 1  # 标记这个数字出现过
    order += cnt * math.factorial(n - i - 1)

# 加上 m
order += m

# 逆康托展开
res = []  # 存储答案
tag = [0 for _ in range(n+1)]  # 用于标记数有没有出现过
tag[0] = 1
for i in range(n - 1):
    cnt = int(order / math.factorial(n-(i + 1)))  # 计算当前这个位置应当有几个数小
    t = 1
    while cnt:  # 找出前cnt个比他小且还未出现的数
        if not tag[t]:
            cnt -= 1
        t += 1
    while tag[t]:  # 如果这个数出现过了，就向后移动
        t += 1
    # 找到了这个位置应该放的数
    tag[t] = 1  # 出现过了
    res.append(t)  # 加入这个数
    order = order % math.factorial(n-(i + 1))
# 找到最后一位还没出现的数
for i in range(n+1):
    if not tag[i]:
        res.append(i)
        break
# 按要求输出

for item in res:
    print(item, end=' ')

# 满分代码
# def hanshu():
#     global ls
#     for i in range(n-2,-1,-1):
#         if ls[i]<ls[i+1]:
#             break
#     for j in range(n-1,i,-1):
#         if ls[j]>ls[i]:
#             break
#     ls[i],ls[j]=ls[j],ls[i]
#     ls1=ls[:i+1]
#     ls2=ls[i+1:]
#     ls2.sort()
#     ls=ls1+ls2
# n=int(input().strip())
# m=int(input().strip())
# ls=[int(i) for i in input().strip().split()]
# for i in range(m):
#     hanshu()
# for i in ls:
#     print(i,end=" ")
