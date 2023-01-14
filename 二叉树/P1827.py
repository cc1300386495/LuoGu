# P1827 [USACO3.4] 美国血统 American Heritage
# 该题建议手动模拟一下
# 前序遍历的第一个字母，是二叉树的根节点
# 然后在中序遍历中,根节点的左右两边就是左子树和右子树
# 依次按前序遍历的字母，寻找子树的根节点
# 循环递归即可
# 一定要先递归左子树再递归右子树

midle = input().strip()
left = input().strip()
n = len(left)

# 根据后序遍历，我们可以递归前序遍历中每个字母作为根节点的子树


def find(l1, l2, l3, l4):
    # l1,l2是子树在中序遍历中的范围；
    # l3,l4是前序遍历中的范围
    if l1 > l2 or l3 > l4:
        return
    for q in range(l1, l2+1):
        if midle[q] == left[l3]:
            # 第一次写的时候没有l3,l4，就会导致在找根节点的左子树时，找不到左子树的根节点
            # 但不难发现，根节点的右子树的所有节点输出完后才会输出左子树的根节点
            find(l1, q-1, l3+1, l3+q-l1)
            find(q+1, l2, l3+q-l1+1, l4)
    print(left[l3], end='')


find(0, n-1, 0, n-1)
