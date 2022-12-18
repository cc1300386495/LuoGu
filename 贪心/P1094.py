# P1094 [NOIP2007 普及组] 纪念品分组
# 想要分组数最少，那么尽量让每组纪念品都放两个
# 可以考虑使用双指针算法

w = int(input())
n = int(input())

values = []
for i in range(n):
    values.append(int(input()))

# 先让价格从大到小排序
values.sort()

left, right = 0, n-1

res = 0
while left <= right:
    if values[left] + values[right] <= w:
        res += 1
        right -= 1
        left += 1
    else:
        res += 1
        right -= 1

print(res)
