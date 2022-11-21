# P1152 欢乐的跳
# 继续使用桶排，计算完所有的差后，检查是不是所有的都存在即可

nums = list(map(int, input().split()))
n = nums.pop(0)
records = [0 for _ in range(n)]
records[0] = 1  # 手动置1，表示已经存在

for i in range(n-1):
    c = abs(nums[i] - nums[i+1])
    # 可知，n个数的数组中相邻两个数的差有n-1个，若满足“欢乐的跳”则一个差必然只出现一次
    if c > n - 1:  # 差可能会越界~
        print("Not jolly")
        exit()  # 退出程序
    records[c] += 1
    if records[c] > 1:
        print("Not jolly")
        exit()  # 退出程序

for item in records:
    if item == 0:  # 有一个差没出现
        print("Not jolly")
        exit()  # 退出程序
print("Jolly")
