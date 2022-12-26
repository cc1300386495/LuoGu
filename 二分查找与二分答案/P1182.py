# P1182 数列分段 Section II

n, m = map(int, input().split())

nums = list(map(int, input().split()))


def judge(mid):
    # 分成的几段
    t = 1
    # 当前段的和
    s = 0
    i = 0
    while i < n:
        # 当前段的和还没超过最大值
        if s + nums[i] <= mid:
            s += nums[i]
            i += 1
        else:
            if nums[i] > mid:
                return False
            else:
                s = 0
                t += 1
    if t > m:
        return False
    else:
        return True


left, right = max(nums), sum(nums)
res = 0
while left <= right:
    mid = (left + right) // 2
    if judge(mid):
        res = mid
        right = mid - 1
    else:
        left = mid + 1
print(res)
