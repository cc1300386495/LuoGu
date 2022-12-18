# P1208 [USACO1.3]混合牛奶 Mixing Milk

n, m = map(int, input().split())

milks = []
for i in range(m):
    p, a = map(int, input().split())
    milks.append([p, a])

milks.sort(key=lambda x: x[0])

res = 0

for milk in milks:
    if n >= milk[1]:
        n -= milk[1]
        res += milk[1] * milk[0]
    else:
        res += milk[0] * n
        n = 0
    if n == 0:
        break

print(res)
