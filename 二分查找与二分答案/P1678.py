# P1678 烦恼的高考志愿
# 二分找学校
m, n = map(int, input().split())

a = list(map(int, input().split()))
a.sort()

b = list(map(int, input().split()))

res = 0


def find(left, right, score):
    while left < right:
        mid = (left + right + 1) // 2
        if a[mid] < score:
            left = mid
        else:
            right = mid - 1
    return left


for i in range(n):
    # 先找到小于估分的最高分数线
    temp = find(0, m-1, b[i])
    # 再比较大于估分的最低分数线
    if temp + 1 < m and abs(b[i] - a[temp]) > abs(b[i] - a[temp+1]):
        res += abs(b[i] - a[temp+1])
    else:
        res += abs(b[i] - a[temp])

print(res)
