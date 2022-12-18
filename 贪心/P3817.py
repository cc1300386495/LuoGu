# P3817 小A的糖果
# 可以这样考虑：对于每一个糖果盒都首先要把吃成小于等于x的情况。
# 然后从前向后进行分析
# 如果第一个糖果盒和第二个糖果盒加起来大于x，那么显然吃第二个糖果盒收益是更大的。依次往后推即可

n, x = map(int, input().split())
nums = list(map(int, input().split()))

res = 0
# 首先吧所有糖果盒吃成小于x
for i in range(n):
    if nums[i] > x:
        res += nums[i] - x
        nums[i] = x

# 吃糖果，优先吃后面的
for i in range(1, n):
    if nums[i-1] + nums[i] > x:
        res += (nums[i-1] + nums[i] - x)
        nums[i] = x - nums[i-1]


print(res)
