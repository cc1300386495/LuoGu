# P2058 [NOIP2016 普及组] 海港
# 滑动窗口维护24小时内的船。但是发现每个船很大
# 弹出队头时还得处理船的人，那么就得存储每个船的人数
# 所以一个很巧妙的思路就是把人放进队列里，而不是放船
# 这样就能边读边输出了

from collections import deque

n = int(input())

q = deque()

# 统计队列中每个国籍的人数
nums = [0 for _ in range(100100)]

res = 0

for _ in range(n):
    # 读取每艘船的信息
    line = list(map(int, input().split()))
    t, k = line[0], line[1]
    # 再把每个人添加进队列
    # 每个人用一个列表表示，包含到达时间和国籍两个信息
    for i in range(2, k+2):
        # 如果当前这个人的国籍的人数为0，那么res+1
        if nums[line[i]] == 0:
            res += 1
        nums[line[i]] += 1
        q.append([t, line[i]])
    # 处理时间超过24小时的人
    while q[-1][0] - q[0][0] >= 86400:
        movePeople = q.popleft()
        nums[movePeople[1]] -= 1
        if nums[movePeople[1]] == 0:
            res -= 1
    print(res)
