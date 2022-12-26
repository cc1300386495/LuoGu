# P1163 银行贷款

a, b, c = map(int, input().split())

left, right = 0, 10000

while right - left > 0.0001:
    mid = (left + right) / 2
    # 未换钱总数
    w = a
    for i in range(c):
        w = w - b + w * (mid / 100)
    if w > 0.0001:
        right = mid
    else:
        left = mid
print("%.1f" % left)
