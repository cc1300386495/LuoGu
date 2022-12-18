# P1478 陶陶摘苹果（升级版）
# 一度觉得自己理解错题意了。。。。

n, s = map(int, input().split())
a, b = map(int, input().split())

apples = []

for i in range(n):
    x, y = map(int, input().split())
    apples.append([x, y])

apples.sort(key=lambda x: x[1])

res = 0

for apple in apples:
    if a + b >= apple[0] and s >= apple[1]:
        res += 1
        s -= apple[1]

print(res)
