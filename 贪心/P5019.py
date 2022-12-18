# P5019 [NOIP2018 提高组] 铺设道路
# 贪心求解,可以理解成尽量先铺成等高

n = int(input())


deep = [0] + (list(map(int, input().split())))
res = 0

for i in range(1, n+1):
    if deep[i] > deep[i-1]:
        res += (deep[i] - deep[i-1])


print(res)
