# P1996 约瑟夫问题
# n比较小，所以可以用一个数组标记每个人是否出列

n, m = map(int, input().split())

# 判断每个人是否出列
vis = [0 for _ in range(n)]
p = 0
count = 0

while p < n:
    for i in range(n):
        if vis[i] == 0:
            count += 1
            if count == m:
                count = 0
                print(i+1, end=' ')
                vis[i] = 1
                p += 1
