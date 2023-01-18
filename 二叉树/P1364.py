# P1364 医院设置
# 总结来说：敌进我退
# 首先，任选一个节点，记录以它为医院的总距离
# 然后，递归他的每一个节点，敌进我退！

n = int(input())

# 记录节点
nodes = [[0, 0, 0] for i in range(n+1)]

for i in range(1, n+1):
    nodes[i] = list(map(int, input().split()))


# 记录以节点i为根的子树的权重之和
size = [nodes[i][0] for i in range(n+1)]


def setSize(i):
    global size
    if nodes[i][1] != 0:
        size[i] += setSize(nodes[i][1])
    if nodes[i][2] != 0:
        size[i] += setSize(nodes[i][2])
    return size[i]


setSize(1)

# 记录以节点i为医院时需要的距离
f = [0 for i in range(n+1)]
# 以根节点为医院时的总距离
f[1] = sum(size[2:])
# 如果我们把根节点的右儿子节点2作为医院
# 那么根节点的右子树需要的距离减1，而其他节点的距离都需要+1
# 按照这个规律，处理节点所有即可


def setDistance(i):
    if nodes[i][1] != 0:
        f[nodes[i][1]] = f[i] - size[nodes[i][1]] + \
            (size[1] - size[nodes[i][1]])
        setDistance(nodes[i][1])
    if nodes[i][2] != 0:
        f[nodes[i][2]] = f[i] - size[nodes[i][2]] + \
            (size[1] - size[nodes[i][2]])
        setDistance(nodes[i][2])


setDistance(1)
print(min(f[1:]))
