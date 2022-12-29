# P2895 [USACO08FEB]Meteor Shower S
# 一道普通的广度搜索
# 维护一个二维数组，判断坐标x,y的地方什么时候有陨石降落

m = int(input())

# 记录每个地方陨石到达的最早时间
record = [[2000 for _ in range(1010)] for _ in range(1010)]

for _ in range(m):
    x, y, t = map(int, input().split())
    record[x][y] = min(record[x][y], t)
    # 震动波
    for move_x, move_y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if x + move_x >= 0 and y + move_y >= 0:
            record[x + move_x][y +
                               move_y] = min(record[x + move_x][y + move_y], t)

# 记录到达的最早时间
times = [[-1 for i in range(1010)] for i in range(1010)]
times[0][0] = 0
q = [[0, 0]]


while q:
    loc_x, loc_y = q.pop(0)
    time = times[loc_x][loc_y]
    for move_x, move_y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        # 没越界且没走过
        if loc_x + move_x >= 0 and loc_y + move_y >= 0 and times[loc_x + move_x][loc_y+move_y] == -1:
            # 如果没有陨石坠落，说明安全
            if record[loc_x + move_x][loc_y+move_y] == 2000:
                print(time + 1)
                exit()
            #  如果走到那块陆地的时间早于陨石降落的世界
            if record[loc_x + move_x][loc_y+move_y] > time + 1:
                times[loc_x + move_x][loc_y+move_y] = time + 1
                q.append([loc_x + move_x, loc_y+move_y])
print(-1)
