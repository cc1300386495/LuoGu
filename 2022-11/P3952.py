# P3952 [NOIP2017 提高组] 时间复杂度

n = int(input())

while n:
    t, s = input().split()
    t = int(t)
    if s[2] == '1':
        s = 0  # O(n ^ 0) == 1
    else:
        s = int(s[-2])
    v = []  # 存储变量
    m = 0  # 统计复杂度的次数
    d = 0  # 记录F和E是否匹配
    tag = 0  # 标记三种结果
    for _ in range(t):
        line = list(input().split())
        if tag == 1:
            continue
        if line[0] == 'F':
            d += 1  # 多一个F
            if line[1] not in v:  # 变量还未定义
                v.append(line[1])
            else:  # 变量重复
                tag = 1
                continue
            if line[-2] == 'n':
                continue
            if line[-1] == 'n':
                m += 1
        elif line[0] == 'E':
            d -= 1
        if d < 0:  # E先出现
            tag = 1
        if _ != t - 1 and d == 0:  # 还没读到第一行，已经匹配完了
            v = []  # 存储变量
            m = 0  # 统计复杂度的次数
    if tag:  # F 和 E 不匹配
        print("ERR")
    elif s == m:
        print("Yes")
    else:
        print("No")
    n -= 1
