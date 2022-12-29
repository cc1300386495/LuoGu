# P1443 马的遍历
# 广度搜索，按要求模拟即可
# 注意：马走日！

n, m, x, y = map(int, input().split())
x, y = x-1, y-1
# 先默认全都到达不了

needs = [[-1 for i in range(m)] for i in range(n)]
needs[x][y] = 0
# 把起始位置添加进队列
q = [[x, y]]

# 只要队列不空
while q:
    # 当前在的位置
    loc_x, loc_y = q.pop(0)
    # 到达当前位置需要的步数
    step = needs[loc_x][loc_y]
    # 开始判断能跳到哪些地方
    if -1 < loc_x + 1 < n and -1 < loc_y - 2 < m and needs[loc_x + 1][loc_y - 2] == -1:
        # 说明没越界，且还没到达
        needs[loc_x + 1][loc_y - 2] = step + 1
        q.append([loc_x + 1, loc_y - 2])

    if -1 < loc_x + 2 < n and -1 < loc_y - 1 < m and needs[loc_x + 2][loc_y - 1] == -1:
        # 说明没越界，且还没到达
        needs[loc_x + 2][loc_y - 1] = step + 1
        q.append([loc_x + 2, loc_y - 1])

    if -1 < loc_x - 1 < n and -1 < loc_y + 2 < m and needs[loc_x - 1][loc_y + 2] == -1:
        # 说明没越界，且还没到达
        needs[loc_x - 1][loc_y + 2] = step + 1
        q.append([loc_x - 1, loc_y + 2])

    if -1 < loc_x - 2 < n and -1 < loc_y + 1 < m and needs[loc_x - 2][loc_y + 1] == -1:
        # 说明没越界，且还没到达
        needs[loc_x - 2][loc_y + 1] = step + 1
        q.append([loc_x - 2, loc_y + 1])

    if -1 < loc_x - 1 < n and -1 < loc_y - 2 < m and needs[loc_x - 1][loc_y - 2] == -1:
        # 说明没越界，且还没到达
        needs[loc_x - 1][loc_y - 2] = step + 1
        q.append([loc_x - 1, loc_y - 2])

    if -1 < loc_x - 2 < n and -1 < loc_y - 1 < m and needs[loc_x - 2][loc_y - 1] == -1:
        # 说明没越界，且还没到达
        needs[loc_x - 2][loc_y - 1] = step + 1
        q.append([loc_x - 2, loc_y - 1])

    if -1 < loc_x + 1 < n and -1 < loc_y + 2 < m and needs[loc_x + 1][loc_y + 2] == -1:
        # 说明没越界，且还没到达
        needs[loc_x + 1][loc_y + 2] = step + 1
        q.append([loc_x + 1, loc_y + 2])

    if -1 < loc_x + 2 < n and -1 < loc_y + 1 < m and needs[loc_x + 2][loc_y + 1] == -1:
        # 说明没越界，且还没到达
        needs[loc_x + 2][loc_y + 1] = step + 1
        q.append([loc_x + 2, loc_y + 1])

for i in range(n):
    for j in range(m):
        print("%-5d" % needs[i][j], end=' ')
    print()
