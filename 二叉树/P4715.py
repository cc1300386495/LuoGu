# P4715 【深基16.例1】淘汰赛
# 构造一个完全二叉树，从叶子节点更新即可

n = int(input())
line = [0] + list(map(int, input().split()))

# 记录每场比赛的结果，0表示还没比
tree = [0 for i in range(2 ** (n + 1))]

t = -1
for i in range(2**n, 0, -1):
    tree[t] = i
    t -= 1


def find(n):
    # 如果第n场比赛还没有结果，就看子树
    if tree[n] == 0:
        if line[find(2*n)] > line[find(2*n+1)]:
            tree[n] = find(2*n)
        else:
            tree[n] = find(2*n+1)
    return tree[n]


if find(1) == find(2):
    print(find(3))
else:
    print(find(2))
