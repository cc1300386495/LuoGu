# P2036 [COCI2008-2009#2] PERKET
# 数据小于10，因此可以暴力搜索，每个配料选还是不选

m = int(input())

seasonings = []

for _ in range(m):
    seasonings.append(list(map(int, input().split())))

res = 99999999
count = 0  # 统计选了几种配料，要保证至少一种

s = 1
b = 0


def dfs(n, tag):  # tag用于标记选不选这个配料
    global s, b, count, res
    if tag:
        count += 1
    if n == m:
        return
    if tag:
        if count == 1:
            s = seasonings[n][0]
        else:
            s *= seasonings[n][0]
        b += seasonings[n][1]
        res = min(res, abs(s-b))
        res = min(res, abs(seasonings[n][0]-seasonings[n][1]))
        dfs(n+1, True)
        count -= 1  # 回溯
        if n+1 < m:
            s //= seasonings[n+1][0]
            b -= seasonings[n+1][1]
        dfs(n+1, False)
    else:
        dfs(n+1, True)
        count -= 1  # 回溯
        if n+1 < m:
            if count == 0:
                s = 0
            else:
                s //= seasonings[n+1][0]
            b -= seasonings[n+1][1]
        dfs(n+1, False)


if m == 1:
    print(abs(seasonings[0][0]-seasonings[0][1]))
    exit()

dfs(0, True)
count = 0
s = 0
b = 0

dfs(0, False)
print(res)
