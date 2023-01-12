# P4913 【深基16.例3】二叉树深度
# 构造结点，然后递归
import sys
sys.setrecursionlimit(1000000)
# 如果不加上面两行，case1，4会re

n = int(input())

nodes = [[] for _ in range(n+1)]

for i in range(1, n+1):
    l, r = map(int, input().strip().split(' '))
    nodes[i] = [l, r]

m = 0


def deep(i, h):
    global m
    m = max(m, h)
    if nodes[i][0] != 0:
        deep(nodes[i][0], h+1)
    if nodes[i][1] != 0:
        deep(nodes[i][1], h+1)


deep(1, 1)

print(m)
