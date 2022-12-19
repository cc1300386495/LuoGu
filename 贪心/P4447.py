# P4447 [AHOI2018初中组]分组
# 用栈来表示每个分组，为了保证组内人数尽可能大 ，应当保证如果某个队员能够同时加入多个组，将它放入人数较少的那组
# 难点在于，怎么找到那个人数较少的组？越往后的组人数肯定越少


n = int(input())

values = list(map(int, input().split()))

# 排序
values.sort()

# 存储所有的栈
all_groups = []
for i in range(n):
    if len(all_groups) == 0:
        t = [values[i]]
        all_groups.append(t)
    else:
        tag = True
        # 从后往前找，可以插入的人数最少的组
        for j in range(len(all_groups)-1, -1, -1):
            if all_groups[j][-1] + 1 == values[i]:
                tag = False
                all_groups[j].append(values[i])
                break
        if tag:
            # 单独创建一个分组
            all_groups.append([values[i]])
length = [len(group) for group in all_groups]
print(min(length))
