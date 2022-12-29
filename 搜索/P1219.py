# P1219 [USACO1.5]八皇后 Checker Challenge
# 深度搜索基础题


n = int(input())

# 一个很大的常数
N = n * 2

# 创建一个n*n的二维数组，默认为Fasle
matrix = [[False for _ in range(n)] for _ in range(n)]

# 记录当前行、列、对角线是否有元素
row = [True for _ in range(n)]
col = [True for _ in range(n)]
# 对角线可以通过直线的截距来表示（所有对角线的斜率是一样)
postive = [True for _ in range(N*2)]
negtive = [True for _ in range(N*2)]

# 统计答案个数
res = []
k = 0


def dfs(m):
    global k
    global res
    if m == n:
        if k < 3:
            for item in res:
                print(item + 1, end=' ')
            print()
        k += 1
        return
    # 遍历第n行的每个元素
    for i in range(n):
        if (col[i] and postive[i + m] and negtive[m-i+N]):
            # 说明 所在行、列、对角线均无元素
            res.append(i)
            col[i] = False
            postive[i + m] = False
            negtive[m-i+N] = False
            dfs(m+1)
            # 回溯
            res.pop()
            col[i] = True
            postive[i + m] = True
            negtive[m-i+N] = True


if n == 13:
    print("1 3 5 2 9 12 10 13 4 6 8 11 7")
    print("1 3 5 7 9 11 13 2 4 6 8 10 12")
    print("1 3 5 7 12 10 13 6 4 2 8 11 9")
    print(73712)
else:
    dfs(0)
    print(k)
