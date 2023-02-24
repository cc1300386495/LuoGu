# P1918 保龄球
# 题目保证各个位置的瓶子数不同。
# 所以可以通过字典完成 瓶子数目->位置 的映射

n = int(input())

nums = list(map(int, input().split()))

d = {}
for i in range(1, n+1):
    d[nums[i-1]] = i

q = int(input())
for i in range(q):
    need = int(input())
    print(d.get(need, 0))
