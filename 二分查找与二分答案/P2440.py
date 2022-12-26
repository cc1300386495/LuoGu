# P2440 木材加工

n, k = map(int, input().split())

woods = []
for _ in range(n):
    woods.append(int(input()))

left, right = 0, max(woods)
res = 0
while left + 1 < right:
    # 取中间值作为切割长度
    mid = (left + right) // 2
    # 统计切割出的数量
    t = 0
    for wood in woods:
        t += (wood // mid)
    # 如果数量符合要求，那么可以再切割长一点
    if t >= k:
        left = mid
    else:
        right = mid
print(left)
