# P3405 [USACO16DEC]Cities and States S
# dict求解

n = int(input())
ans = 0
d = {}

for i in range(n):
    s1, s2 = input().split()
    s1 = s1[:2]
    # 先查看有没有s1+s2对应的组
    # 如果没有这个组合,则创建
    if d.get(s1+s2, 0) == 0:
        d[s1+s2] = 1
    else:
        d[s1+s2] = d[s1+s2] + 1
    # 然后检查有没有特殊城市的组合,如果有ans += 1
    if s1 != s2 and d.get(s2+s1, 0):
        ans += d[s2+s1]

print(ans)
