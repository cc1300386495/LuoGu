# P1149 [NOIP2008 提高组] 火柴棒等式
# 这道题的难点在于 如何表示一位以上的数？
# 一开始的想法是，通过深搜，得出n个火柴棍可以摆出哪些数字，再对数字排列组合
# 但后面发现，n<=24，那么如果全部摆1（因为1需要的火柴最少，能摆的位数最多），那么能摆12位
# 不过我们需要摆三个数字，且+ = 需要四个火柴棍
# 因此理论上，我们只需要统计到 1111

n = int(input())

nums_need = [0 for _ in range(10001)]
nums_need[0] = 6
nums_need[1] = 2
nums_need[2] = 5
nums_need[3] = 5
nums_need[4] = 4
nums_need[5] = 5
nums_need[6] = 6
nums_need[7] = 3
nums_need[8] = 7
nums_need[9] = 6

for i in range(10, 100):
    nums_need[i] = nums_need[i//10] + nums_need[i % 10]
for i in range(100, 1000):
    nums_need[i] = nums_need[i//100] + \
        nums_need[(i // 10) % 10] + nums_need[i % 10]
for i in range(1000, 10001):
    nums_need[i] = nums_need[i//1000] + \
        nums_need[(i // 100) % 10] + nums_need[(i // 10) %
                                               10] + nums_need[i % 10]

n -= 4  # 用于摆等号和加号
cnt = 0
for a in range(1112):
    for b in range(1112):
        if nums_need[a] + nums_need[b] + nums_need[a+b] == n:
            print("a:{} b:{}".format(a, b))
            cnt += 1
print(cnt)
