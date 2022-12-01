# P1706 全排列问题
# 遍历每一位的选择即可
# 深度优先写法，注意回溯


n = int(input())
temp = []
tag = [0 for _ in range(n+1)]  # 标记数有没有用过


def dfs(t):  # 选择的数量为t个
    global temp
    if t == n:
        for item in temp:
            print("%5d" % item, end='')  # 要求输出宽度为5
        print()
        return
    for i in range(1, n+1):  # 尝试在这个位置上放每一个数
        if not tag[i]:
            tag[i] = 1
            temp.append(i)
            dfs(t+1)
            # 回溯
            temp.pop()
            tag[i] = 0


dfs(0)
