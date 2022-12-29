# P1135 奇怪的电梯
# 广度搜索：到达每一层有上、下两种选择

N, A, B = map(int, input().split())

k = [0] + list(map(int, input().split()))

res = 0
# 达到楼层需要的按钮次数
needs = [-1 for i in range(N + 10)]

q = []
q.append(A)
needs[A] = 0

while q:
    loc = q.pop(0)
    need = needs[loc]
    if 1 <= loc + k[loc] <= N and needs[loc + k[loc]] == -1:
        # 说明还没到过这层
        needs[loc + k[loc]] = need + 1
        q.append(loc + k[loc])
    if 1 <= loc - k[loc] <= N and needs[loc - k[loc]] == -1:
        # 说明还没到过这层
        needs[loc - k[loc]] = need + 1
        q.append(loc - k[loc])

print(needs[B])
