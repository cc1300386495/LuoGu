# P1090 [NOIP2004 提高组] 合并果子 / [USACO06NOV] Fence Repair G
# 最先合并的堆，需要搬运的次数越多
# 可以利用小根堆(可以看同级目录下 堆.md )来进行求解

# 果子的种类数
n = int(input())
# 记录花费的力气
res = 0
# 用于维护堆的一维数组,尽量开大一点
heap = [0 for _ in range(100000)]
# 用于记录当前数组大小
size = 0


# 手写堆
def down(u):
    t = u
    if 2 * u <= size and heap[2 * u] < heap[t]:
        t = 2 * u
    if 2 * u + 1 <= size and heap[2 * u + 1] < heap[t]:
        t = 2 * u + 1
    if t != u:
        heap[t], heap[u] = heap[u], heap[t]
        down(t)


def up(u):
    while u // 2 > 0 and heap[u // 2] > heap[u]:
        heap[u], heap[u//2] = heap[u//2], heap[u]
        u = u // 2


# 各种果子的数目
resline = list(map(int, input().split()))

# 插入堆
for i in range(n):
    size += 1
    heap[size] = resline[i]
    up(size)

while size > 1:
    # 先求出前两个最小的堆
    t1 = heap[1]
    heap[1], heap[size] = heap[size], heap[1]
    size -= 1
    down(1)
    t2 = heap[1]
    heap[1], heap[size] = heap[size], heap[1]
    size -= 1
    down(1)
    # 合并这两个堆花费的力气
    new_all = t1 + t2
    res += new_all

    # 将新合并的堆插入
    size += 1
    heap[size] = new_all
    up(size)

print(res)
