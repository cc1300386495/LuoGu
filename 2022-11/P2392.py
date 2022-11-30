# P2392 kkksc03考前临时抱佛脚
# 因为要保证用时最短，那么我们就得保证左右脑的计算时间要一致。
# 数据量只有20，可以直接暴力搜索。枚举所有情况，暴搜即可

s1, s2, s3, s4 = map(int, input().split())
all_time = 0


def dfs(objects, n, where, all):
    global left, right, res
    if n == all:
        res = min(res, max(left, right))
        return
    if where == 0:
        left += objects[n]
    else:
        right += objects[n]
    dfs(objects, n+1, 0, all)
    if n + 1 < all:
        left -= objects[n+1]  # 回溯

    dfs(objects, n+1, 1, all)
    if n + 1 < all:
        right -= objects[n+1]  # 回溯


objects = list(map(int, input().split()))  # s1每道题需要的时间
left = 0
right = 0
res = 99999999
dfs(objects, 0, 0, s1)
dfs(objects, 0, 1, s1)
all_time += res

objects = list(map(int, input().split()))  # s1每道题需要的时间
left = 0
right = 0
res = 99999999
dfs(objects, 0, 0, s2)
dfs(objects, 0, 1, s2)
all_time += res

objects = list(map(int, input().split()))  # s1每道题需要的时间
left = 0
right = 0
res = 99999999
dfs(objects, 0, 0, s3)
dfs(objects, 0, 1, s3)
all_time += res

objects = list(map(int, input().split()))  # s1每道题需要的时间
left = 0
right = 0
res = 99999999
dfs(objects, 0, 0, s4)
dfs(objects, 0, 1, s4)
all_time += res

print(all_time)
