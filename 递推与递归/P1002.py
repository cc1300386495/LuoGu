# P1002 [NOIP2002 普及组] 过河卒
# 从起点开始递归，向下走或者想左走
# 类似P1002 只是拓展到了2纬，且增加了一下障碍
end_x, end_y, house_x, house_y = map(int, input().split())
count = 0

# TLE 因此采用动态规划进行压缩
# def find(start_x, start_y):
#     global count
#     for x in [0, 1, -1, 2, -2]:
#         if x == 0:
#             y = 0
#             if start_x + x == house_x and start_y + y == house_y:
#                 return  # 到达障碍点
#         if x == 1 or x == -1:
#             for y in [2, -2]:
#                 if start_x + x == house_x and start_y + y == house_y:
#                     return  # 到达障碍点
#         if x == 2 or x == -2:
#             for y in [1, -1]:
#                 if start_x + x == house_x and start_y + y == house_y:
#                     return  # 到达障碍点
#     if start_x > end_x or start_y > end_y:
#         return  # 不可能再到达目的地
#     if start_x == end_x and start_y == end_y:
#         count += 1
#         return
#     find(start_x+1, start_y)
#     find(start_x, start_y+1)


def judge(start_x, start_y):
    # 判断有没有到达障碍点
    for x in [0, 1, -1, 2, -2]:
        if x == 0:
            y = 0
            if start_x + x == house_x and start_y + y == house_y:
                return True  # 到达障碍点
        if x == 1 or x == -1:
            for y in [2, -2]:
                if start_x + x == house_x and start_y + y == house_y:
                    return True  # 到达障碍点
        if x == 2 or x == -2:
            for y in [1, -1]:
                if start_x + x == house_x and start_y + y == house_y:
                    return True  # 到达障碍点
    return False


dp = [[0 for _ in range(end_y+10)] for _ in range(end_x+10)]
dp[0][0] = 1
for i in range(end_x+1):
    for j in range(end_y+1):
        if not judge(i+1, j):
            dp[i+1][j] += dp[i][j]
        if not judge(i, j+1):
            dp[i][j+1] += dp[i][j]


print(dp[end_x][end_y])
