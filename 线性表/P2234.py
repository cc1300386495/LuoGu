# P2234 [HNOI2002]营业额统计
# 先排再找

n = int(input())

nums = []
for i in range(n):
    num = int(input())
    # 记录金额及天数
    nums.append([num, i])

# 按金额排序
nums.sort()

res = 0
for i in range(n):
    value, day = nums[i]
    if day == 0:
        res += value
        continue
    # 找到左边第一个天数小于day的
    valueLeft = 10000000
    for left in range(i-1, -1, -1):
        if nums[left][1] < day:
            valueLeft = nums[left][0]
            break
    # 同理找右边
    valueRight = 10000000
    for right in range(i+1, n):
        if nums[right][1] < day:
            valueRight = nums[right][0]
            break
    tempMin = min(abs(value-valueRight), abs(value-valueLeft))
    res += tempMin
print(res)


# 暴力

# n = int(input())

# nums = []
# for _ in range(n):
#     nums.append(int(input()))

# res = nums[0]

# for i in range(1, len(nums)):
#     temp = abs(nums[i] - nums[0])
#     for j in range(i):
#         temp = min(temp, abs(nums[i] - nums[j]))
#     res += temp

# print(res)
