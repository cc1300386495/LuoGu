# P1032 [NOIP2002 提高组] 字串变换
# 看官方介绍，貌似是个错题~
from collections import deque
A, B = input().split()

changes = []

# 通过try语句来读取不确定的行数
while True:
    try:
        a, b = input().split()
        changes.append([a, b])
    except:
        break

# 记录到达每个字符串需要的最短步数
step = {}
# 判断当前字符串是否出现过
vis = {}

# 队列
q = deque()
# 初始化
q.append(A)
step[A] = 0
vis[A] = 1

while q:
    now_A = q.popleft()
    if now_A == B:
        break
    if step[now_A] > 10:
        break
    for i in range(len(changes)):
        A_i, B_i = changes[i]
        # 说明可以转换
        if A_i in now_A:
            # A_i在now_A的开始下标
            # 注意！！！
            # start = now_A.find(A_i)
            # 子串可能有很多个，如果按上面的写法永远只能替换第一个，所以要改一下
            starts = []
            t = 0
            l = len(A_i)
            while True:
                # 每找到一个子串，就更新find的起始位置
                if now_A.find(A_i, t) != -1:
                    starts.append(now_A.find(A_i, t))
                    t += l
                else:
                    break
            for start in starts:
                # 转换字符串
                newA = now_A[:start] + B_i + now_A[start+l:]
                # 如果这个字符串没有出现过
                if not vis.get(newA, 0):
                    step[newA] = step[now_A] + 1
                    vis[newA] = 1
                    q.append(newA)

t = step.get(B)
if t == None or t <= 0 or t > 10:
    print("NO ANSWER!")
else:
    print(t)
