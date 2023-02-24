# P5266 【深基17.例6】学籍管理
# 字典yyds

d = {}

n = int(input())

for i in range(n):
    line = input().split()
    # 插入学生
    if line[0] == '1':
        d[line[1]] = line[2]
        print("OK")
    elif line[0] == '2':
        if line[1] in d.keys():
            print(d[line[1]])
        else:
            print('Not found')
    elif line[0] == '3':
        if line[1] in d.keys():
            del d[line[1]]
            print("Deleted successfully")
        else:
            print('Not found')
    else:
        print(len(d))
