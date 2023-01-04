# P2404 自然数的拆分问题
# 需要注意到一点：
# 最后拆分出的算式一定是：n//2 + (n2//2 + 1) or n//2 + n2//2
# 按照这个规律进行深度搜索即可

n = int(input())

# 记录当前算式中的数字
record = []


def dfs(i):
    global record
    s = sum(record)
    if s == n:
        # 输出答案
        for index in range(len(record)-1):
            print(record[index], end='+')
        print(record[-1])
        return 0
    if s > n:
        return -1
    # 到了这步说明record还可以加
    for j in range(i, n):
        # 加一个数
        record.append(j)
        t = dfs(j)
        record.pop()
        if t == -1:
            # 如果加上j都大于n的话，那么比j大的数再深搜就没有意义了
            break


if n == 1:
    print(1)
else:
    dfs(1)
