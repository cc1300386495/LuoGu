# P5250 【深基17.例5】木材仓库
# 用字典存储，然后按要求模拟

import bisect
n = int(input())

d = {}
# 统计仓库的木材数量
nums = 0

for i in range(n):
    op, num = map(int, input().split())
    if op == 1:
        if d.get(num, 0) == 1:
            print("Already Exist")
        if d.get(num, 0) == 0:
            d[num] = 1
            nums += 1
    else:
        if d.get(num, 0) == 1:  # 如果有num长度的木材
            print(num)
            d[num] = 0
            nums -= 1
        else:
            # 如果没有，判断仓库是否为空
            if nums == 0:
                print("Empty")
            # 开始依次找
            else:
                i = 1
                while True:
                    if d.get(num-i, 0) == 1:
                        choose = num - i
                        break
                    if d.get(num+i, 0) == 1:
                        choose = num + i
                        break
                    i += 1
                d[choose] = 0
                nums -= 1
                print(choose)

# 平衡树解法

n = int(input())
items = []
for i in range(n):
    tp, length = [*map(int, input().split())]
    if tp == 1:
        idx = bisect.bisect_left(items, length)
        if idx < len(items) and items[idx] == length:
            print('Already Exist')
        else:
            items.insert(idx, length)
    else:
        if len(items) == 0:
            print("Empty")
        else:
            idx = bisect.bisect_left(items, length)

            # idx length
            idxx = 0
            if idx == 0:
                idxx = 0
            elif idx == len(items):
                idxx = idx - 1
            else:
                l, r = length - items[idx - 1], items[idx] - length
                if l <= r:
                    idxx = idx - 1
                else:
                    idxx = idx

            print(items.pop(idxx))
