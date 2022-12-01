# P1781 宇宙总统
# 不断对比当前的输入，保留最大即可

n = int(input())

flag = -1  # 候选人编号
vote = -1  # 拥有的票数

for i in range(n):
    temp = int(input())
    if temp > vote:
        vote = temp
        flag = i + 1
print(flag)
print(vote)
