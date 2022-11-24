# P1036的弱化版

n, r = map(int, input().split())
temp = []


def dfs(i, t):  # 选到了数i，选择的数量为t个
    global cnt
    global temp
    if t == r:
        for item in temp:
            print("%3d" % item, end='')  # 要求输出宽度为3
        print()
        return
    if i > n:
        return
    # 选择这个数
    temp.append(i)
    dfs(i+1, t+1)
    # 回溯，且不选择这个数
    temp.pop()
    dfs(i+1, t)


dfs(1, 0)
