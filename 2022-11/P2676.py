# P2676 [USACO07DEC]Bookshelf B
# 先排序，然后从未选择的当中选择最高的，直至大于B

n, b = map(int, input().split())
records = []

for i in range(n):
    records.append(int(input()))

records.sort(reverse=True)  # 从大到小排

now = 0  # 当前选到第几个
s = 0  # 当前高度

while s < b:
    s += records[now]
    now += 1

print(now)
