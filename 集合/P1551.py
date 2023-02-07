# P1551 亲戚
# 并查集模板题

n, m, q = map(int, input().split())


# 并查集的递归函数
def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]


# 初始时每个人是自己的亲戚
p = [i for i in range(n+1)]

for _ in range(m):
    p1, p2 = map(int, input().split())
    p[find(p1)] = find(p2)

for _ in range(q):
    q1, q2 = map(int, input().split())
    if find(q1) != find(q2):
        print("No")
    else:
        print("Yes")
