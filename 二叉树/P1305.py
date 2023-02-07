# P1305 新二叉树
# 前序遍历，递归实现

n = int(input())

tree = {}
for _ in range(n):
    s = input()
    if _ == 0:
        head = s[0]
    tree[s[0]] = [s[1], s[2]]


def front(node):
    print(node, end='')
    if tree[node][0] != '*':
        front(tree[node][0])
    if tree[node][1] != '*':
        front(tree[node][1])


front(head)
