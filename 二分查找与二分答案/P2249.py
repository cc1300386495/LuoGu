# P2249 【深基13.例1】查找

n, m = map(int, input().split())
nums = list(map(int, input().split()))
questions = list(map(int, input().split()))


def find(target):
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


for i in range(m):
    print(find(questions[i]), end=' ')
