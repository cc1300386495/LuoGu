# P3743 kotori的设备
# 本题难点在于：如何判断可以无限运行？
# 解：只要所有设备的用电速度之和小于充电速度即可
# 因为题意是值充电时间没有限制且换设备充电不消耗时间
# 所有按常规二分解答即可

n, p = map(int, input().split())

devices = []

for _ in range(n):
    devices.append(list(map(int, input().split())))

# 特判，计算总用电速度
s = 0
for i in range(n):
    s += devices[i][0]
if s <= p:
    print(-1)
    exit()


# 判断这个时间能不能完成
def judge(mid):
    # 先计算总的需要补充的电量
    s = 0
    for i in range(n):
        if (devices[i][0] * mid - devices[i][1]) > 0:
            s += (devices[i][0] * mid - devices[i][1])
    # 计算可以充的电量
    t = mid * p

    if s > t:
        return False
    else:
        return True


left, right = 0, 1e10
while right - left >= 0.000001:
    mid = (left + right) / 2
    if judge(mid):
        left = mid
    else:
        right = mid
print("%.10f" % left)
