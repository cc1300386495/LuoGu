# P2678 [NOIP2015 提高组] 跳石头
# 通过二分寻找答案

l, n, m = map(int, input().split())

dis = [0]
for _ in range(n):
    dis.append(int(input()))
# 终点
dis.append(l)


# 判读当前最短距离是否符合要求
def judge(mid):
    # 需要移走的石头数量
    t = 0
    # 起始位置
    i = 1
    now = 0
    while i <= n + 1:
        # 如果小于最短距离，则需要搬走石头
        if dis[i] - dis[now] < mid:
            t += 1
        # 如果满足最小距离，就跳过去
        else:
            now = i
        i += 1
    if t > m:
        return False
    else:
        return True


res = 0
left, right = 0, l
# 二分寻找最短距离
while left <= right:
    mid = (left+right) // 2
    if judge(mid):
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)
