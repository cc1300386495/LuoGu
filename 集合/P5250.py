# P5250 【深基17.例5】木材仓库
# 用字典存储，然后按要求模拟

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
