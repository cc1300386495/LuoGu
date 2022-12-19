# P1080 [NOIP2012 提高组] 国王游戏 题解
# 因为推导证明涉及到的数学公式有点多，详细证明请看题解
# 大致结果就是：按照左右手的乘积排序，越小的越靠前

n = int(input())

peoples = []

# 国王
pl, pr = map(int, input().split())

for _ in range(n):
    peoples.append(list(map(int, input().split())))

peoples.sort(key=lambda x: x[0] * x[1])


leftGoads = pl
res = 0

for i in range(n):
    res = max(res, pl//peoples[i][1])
    pl *= peoples[i][0]

print(res)
