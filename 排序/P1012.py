# P1012 [NOIP1998 提高组] 拼数

# 纯靠字典排序，无法通过绝对样例。因为'321'>'32'，但是32132<32321，所以得额外判断
n = int(input())

nums = list(input().split())
nums.sort(reverse=True)

for i in range(n - 1):
    for j in range(i + 1, n):
        if nums[i] + nums[j] < nums[j] + nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
for s in nums:
    print(s, end='')
