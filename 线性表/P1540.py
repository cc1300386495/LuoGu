# P1540 [NOIP2010 提高组] 机器翻译
# 典型的队列题目

from collections import deque


m, n = map(int, input().split())
# 队列模拟内存
q = deque()

# 记录单词是否在内存当中
vis = [0 for _ in range(1010)]

context = list(map(int, input().split()))

res = 0
# 翻译每个单词
for i in range(n):
    # 如果当前单词在内存中
    if vis[context[i]]:
        continue
    else:
        res += 1
        # 判断是否要移走队头
        if q.__len__() >= m:
            h = q.popleft()
            vis[h] = 0
        q.append(context[i])
        vis[context[i]] = 1

print(res)
