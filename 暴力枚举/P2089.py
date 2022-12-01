# P2089 烤鸡
# 深度搜索
n = int(input())

if n < 10 or n > 30:
    print(0)
    exit()

res = []

# 深搜
record = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 记录方案


def dfs(total, index):  # 当前美味程度，当前遍历到第几个调料
    global res
    if index == 10:  # 最后一个调料遍历完，进行判断
        if total == n:
            res.append(record.copy())  # 如果直接添加record，貌似会添加record的地址，那就无法记录方案了~
    else:
        for i in range(1, 4):  # 每个调料可以放3种情况
            if total + i > n:
                break
            else:
                record[index] = i
                dfs(total + i, index + 1)
                record[index] = 0  # 回溯


dfs(0, 0)
res.sort()
print(len(res))
for item in res:
    for e in item:
        print(e, end=' ')
    print()
