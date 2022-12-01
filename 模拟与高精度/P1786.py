# P1786 帮贡排序
# 按顺序依次排即可
# 分配职位时 首先按帮贡排序，帮贡相同，按输入顺序的先后
# 显示时，按职位排序，职位相同再按等级排，如果等级也相同，则按先后顺序
n = int(input())

m = {
    'BangZhu': 10,
    'FuBangZhu': 9,
    'HuFa': 8,
    'ZhangLao': 7,
    'TangZhu': 6,
    'JingYing': 5,
    'BangZhong': 4
}


persons = []  # 记录帮派成员
for i in range(n):
    name, p, d, g = input().split()
    d = int(d)
    g = int(g)
    persons.append([name, p, d, g, n - i])


# 帮主和副帮主永远在前三个输入，所以可以直接输出
for i in range(3):
    print(persons[i][0], persons[i][1], persons[i][3], sep=' ')


persons = persons[3:]
persons.sort(key=lambda a: [a[2], a[-1]], reverse=True)  # 先根据帮贡排序，再根据顺序排序

# 该循环用于分配职位
for t in range(len(persons)):
    if 0 <= t <= 1:
        persons[t][1] = 'HuFa'
    elif 2 <= t <= 5:
        persons[t][1] = 'ZhangLao'
    elif 6 <= t <= 12:
        persons[t][1] = 'TangZhu'
    elif 13 <= t <= 37:
        persons[t][1] = 'JingYing'
    else:
        persons[t][1] = 'BangZhong'

# 分配好后，再次进行排序
persons.sort(key=lambda x: (m[x[1]], x[3], x[4]),
             reverse=True)  # 先按职位，再按等级，最后按出现的顺序


# 输出
for i in range(len(persons)):
    print(persons[i][0], persons[i][1], persons[i][3], sep=' ')
