# P4387 【深基15.习9】验证栈序列
# 直接模拟即可

n = int(input())


def judge(pushed, poped):
    newStack = []
    t = 0
    # 模拟每一次入栈
    i = 0
    for i in range(len(pushed)):
        # 如果当前入栈的数恰好对应此刻出栈序列的数，那么就直接push-pop
        if pushed[i] == poped[t]:
            t += 1
            # 此时有可能newStack的栈顶元素对应poped[t]
            while newStack and newStack[-1] == poped[t]:
                newStack.pop()
                t += 1
        else:
            # 先存着
            newStack.append(pushed[i])
    while len(newStack):
        temp = newStack.pop()
        if temp == poped[t]:
            t += 1
    if t < len(poped):
        return False
    else:
        return True


for _ in range(n):
    m = int(input())
    pushed = list(map(int, input().split()))
    poped = list(map(int, input().split()))
    if judge(pushed, poped):
        print("Yes")
    else:
        print("No")
