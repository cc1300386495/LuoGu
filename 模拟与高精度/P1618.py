# P1618 三连击（升级版）
# 枚举所有的组合，然后判断
A, B, C = map(int, input().split())

tag = True  # 当前没有答案
res = [0 for _ in range(9)]  # 表示分成的三位数
nums = [0 for _ in range(10)]  # 负责标记数i有没有使用，0表示没有使用


def dfs(n):
    global tag
    if n == 9:
        n1 = res[0] * 100 + res[1]*10 + res[2]
        n2 = res[3] * 100 + res[4]*10 + res[5]
        n3 = res[6] * 100 + res[7]*10 + res[8]
        if n1/n3 == A/C and n2/n3 == B/C and n1/n2 == A/B:
            tag = False  # 有答案，后续就不用输出 No！！！
            print(n1, n2, n3, sep=' ')
    else:
        for i in range(1, 10):
            if not nums[i]:
                res[n] = i  # 第n位放i
                nums[i] = 1  # 被使用了
                dfs(n+1)
                nums[i] = 0  # 回溯


dfs(0)
if tag:  # 说明没找到答案
    print("No!!!")
