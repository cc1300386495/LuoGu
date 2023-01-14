# P5076 【深基16.例7】普通二叉树（简化版）
# 二叉搜索树
# 参考：https://www.cnblogs.com/do-while-true/p/13566274.html

# 定义节点
class Node(object):
    def __init__(self):
        # 节点的值
        self.val = 0
        # 节点左子树的下标
        self.ls = 0
        # 节点右子树的下标
        self.lr = 0
        # 当前节点的值出现了几次
        self.cnt = 0
        # 本身及子树的大小
        self.size = 0


q = int(input().strip())

bst = [Node() for _ in range(q+100)]

# 统计节点个数
count = 0


def add(x, v):
    # x是节点的下标，v是需要添加的值
    # 递归到该节点说明v一定会插进以x节点为根节点的子树当中
    global count
    bst[x].size += 1
    if bst[x].val == v:
        bst[x].cnt += 1
    elif bst[x].val > v:
        # 插进左子树
        # 如果没有左子树
        if bst[x].ls == 0:
            count += 1
            bst[x].ls = count
            bst[count].val = v
            bst[count].size = 1
            bst[count].cnt = 1
        else:
            add(bst[x].ls, v)
    else:
        # 插进左子树
        # 如果没有左子树
        if bst[x].lr == 0:
            count += 1
            bst[x].lr = count
            bst[count].val = v
            bst[count].size = 1
            bst[count].cnt = 1
        else:
            add(bst[x].lr, v)


def findHead(x, v, ans):
    # 寻找小于v的最大的数
    if bst[x].val >= v:
        if bst[x].ls == 0:
            return ans
        else:
            return findHead(bst[x].ls, v, ans)
    else:
        if bst[x].lr == 0:
            return bst[x].val
        return findHead(bst[x].lr, v, bst[x].val)


def findTail(x, v, ans):
    # 大于v且最小的数
    if bst[x].val <= v:
        if bst[x].lr == 0:
            return ans
        else:
            return findTail(bst[x].lr, v, ans)
    else:
        if bst[x].ls == 0:
            return bst[x].val
        return findTail(bst[x].ls, v, bst[x].val)


def findRank(x, v):
    # 按值找排名
    # 统计比v小的数量
    if x == 0:
        return 0
    if bst[x].val == v:
        return bst[bst[x].ls].size
    if bst[x].val > v:
        return findRank(bst[x].ls, v)
    else:
        # 如果当前节点值比val小了，我们就去它的右子树找val，同时加上左子树的大小和这个节点的值出现次数
        return findRank(bst[x].lr, v) + bst[bst[x].ls].size + bst[x].cnt


def findVal(x, rk):
    if x == 0:
        return 2147483647
    if bst[bst[x].ls].size >= rk:
        return findVal(bst[x].ls, rk)
    if (bst[bst[x].ls].size+bst[x].cnt) >= rk:
        return bst[x].val
    else:
        return findVal(bst[x].lr, rk-bst[bst[x].ls].size-bst[x].cnt)


for _ in range(q):
    op, x = map(int, input().split())
    if op == 5:
        if count == 0:
            count += 1
            bst[count].size = 1
            bst[count].cnt = 1
            bst[count].val = x
        else:
            add(1, x)
    elif op == 1:
        print(findRank(1, x)+1)
    elif op == 2:
        print(findVal(1, x))
    elif op == 3:
        print(findHead(1, x, -2147483647))
    else:
        print(findTail(1, x, 2147483647))
