# P1102 A-B 数对
# 二分解法
# 还可以用哈希表，但跟这个目录更没关系了。。。。

n, c = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()


def find_left(target):
    left, right = 0, n-1
    while left < right:
        mid = (left + right)//2
        if nums[mid] >= target:
            right = mid
        if nums[mid] < target:
            left = mid + 1
    if nums[left] == target:
        return left + 1
    else:
        return -1


def find_right(target):
    left, right = 0, n-1
    while left < right:
        mid = (left + right)//2 + 1
        if nums[mid] <= target:
            left = mid
        if nums[mid] > target:
            right = mid - 1
    if nums[left] == target:
        return left + 1
    else:
        return -1


res = 0

for i in range(n):
    left_idex = find_left(nums[i] + c)
    if left_idex != -1:
        right_index = find_right(nums[i] + c)
        res += (right_index - left_idex + 1)

print(res)
