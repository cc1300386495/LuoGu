# P1525 [NOIP2010 提高组] 关押罪犯
# 先把影响力从大到小排序，尽量拆开影响力大的

n, m = map(int, input().split())
record = []
for i in range(m):
    line = list(map(int, input().split()))
    record.append(line)
record.sort(key=lambda x: -x[2])


p = [i for i in range(n)]


def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]


def add(x, y):
    x = find(p[x])
    y = find(p[y])
    p[x] = y


# 存每个人的敌人
op = [-1 for _ in range(n)]

for i in range(m+1):
    if i == m:
        # 如果i==m，说明前面m对罪犯已经合理的分配，且不会发生冲突
        print(0)
        break
    a, b, c = record[i]
    a = a - 1
    b = b - 1
    # 如果这两个在同一监狱
    if find(a) == find(b):
        print(c)
        break
    # 如果不在同一个监狱
    else:
        # 看a的敌人是谁
        # 如果还没记录敌人
        if op[a] == -1:
            op[a] = b
        # 如果有敌人了，就合并
        else:
            add(b, op[a])
        # 同理对待b
        # 如果还没记录敌人
        if op[b] == -1:
            op[b] = a
        # 如果有敌人了，就合并
        else:
            add(a, op[b])
