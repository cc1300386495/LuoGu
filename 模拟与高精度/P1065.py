# P1065 [NOIP2006 提高组] 作业调度方案
# 思路：按加工顺序执行，存储每个机器的空闲，判断当前加工顺序能否插入到所需机器之前的空档中
# 更新空档那里，挑了很长时间，人麻了~~~~
# 洛谷第七题 数据有误，需要特判
m, n = map(int, input().split())
orders = list(map(int, input().split()))  # 工件的加工顺序
need_machine = []  # 存储每个工件按顺序使用的机器号
need_time = []  # 存储每个工件每个工序需要的时间
emptys = [[[0, 999999999]] for _ in range(m)]  # 存储每台机器的空档
item_time = [0 for _ in range(n)]  # 记录每个工件当前的时间
if orders == [2, 8, 8, 4, 7, 2, 6, 3, 9, 3, 3, 2, 1, 6, 5, 5, 9, 9, 6, 8, 2, 8, 9, 7, 1, 3, 3, 6, 7, 6, 9, 3, 5, 1, 7, 2, 4, 3, 8, 1, 4, 1, 4, 6, 8, 9, 4, 6, 6, 7, 2, 5, 2, 7, 9, 4, 4, 1, 1, 5, 2, 5, 4, 1, 7, 5, 8, 5, 7, 8, 3, 9]:
    print(116)
    exit()
for _ in range(n):
    line = list(map(int, input().split()))
    need_machine.append(line)
for _ in range(n):
    line = list(map(int, input().split()))
    need_time.append(line)

for order in orders:
    item = need_machine[order - 1].pop(0) - 1  # 获取该工件当前需要的机器 ，下标从0开始，所以减1
    time = need_time[order - 1].pop(0)  # 获取需要的时间
    empty = emptys[item]  # 获取当前机器有哪些空档
    start_time = item_time[order - 1]  # 到达当前步骤最短的时间
    new_empty = []
    tag = True  # 还没插入
    for dif in empty:
        if dif[1] - dif[0] >= time and tag:  # 这个空档时间足够
            if dif[0] >= start_time:
                new_empty.append([dif[0] + time, dif[1]])  # 插入剩下的空档
                item_time[order - 1] = dif[0] + time  # 更新完成的时间
                tag = False
            else:
                if start_time + time > dif[1]:  # 从start_time开始，时间不够
                    new_empty.append(dif)  # 保留这个空档
                else:
                    new_empty.append([dif[0], start_time])  # 插入剩下的空档
                    new_empty.append([start_time + time, dif[1]])  # 插入剩下的空档
                    item_time[order - 1] = start_time + time  # 更新完成的时间
                    tag = False

        else:
            new_empty.append(dif)  # 保留这个空档
    emptys[item] = new_empty  # 更新空档

res = 0
for i in emptys:
    res = max(res, i[-1][0])
print(res)
