# P1249 最大乘积
# 思路
# 预备知识：乘数越多越好
# 因为乘1对增大没有任何意义，所以从2开始递增，2+3+~+t，直至sum >= target
# 如果sum==target 显然，此时是乘数最多的一种方案了
# 如果sum > target 呢？ 也很简单，不难证明，1<= sum - target < t,所以我们只要将乘数中的sum - target这个值去掉即可，便保证了乘数最多。
# 如果sum-target == 1 的话，只需要把2给删去，然后最后一个乘数+1即可
n = int(input())
f = []  # 存储乘数
s = 0  # sum
for i in range(2, n+1):
    s += i
    f.append(i)
    if s >= n:
        break

if s-n == 1:
    f.pop(0)
    f[-1] += 1

res = 1
for item in f:
    if s-n != item:
        print(item, end=' ')
        res *= item
print()
print(res)

# 挖坑一个思路（暂时不会怎么记录选择的物品，所以没用这个思路~）
# 思路：动态规划
# 借助01背包问题，我们可以找到在1~n中，容纳量为n(即和为n)能装的最大价值。
# 背包问题求的是价值之和最大，而题目要求乘积最大，因此可以借助ln函数的性质
# ln(a*b) = ln(a) + ln(b) 因此，我们只要将价值转换为ln即可。
