# P3853 [TJOI2007]路标设置
# 和P2678类似

l, n, k = map(int, input().split())

locs = list(map(int, input().split()))


def judge(mid):
    t = 0
    i = 1
    now = 0
    while i < n:
        if now + mid < locs[i]:
            now += mid
            t += 1
            if t > k:
                return False
        else:
            now = locs[i]
            i += 1
    if t > k:
        return False
    else:
        return True


left, right = 0, l
while left <= right:
    mid = (left+right) // 2
    if judge(mid):
        res = mid
        right = mid - 1
    else:
        left = mid + 1

print(res)
