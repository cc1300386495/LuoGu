# P3613 【深基15.例2】寄包柜
# 直接开大数组，不可取
# 因为保证查询的格子一定存取过，所以只记录存过的即可
# hash~yyds

n, q = map(int, input().split())

d = {}

for _ in range(q):
    line = list(map(int, input().split()))
    if line[0] == 1:
        # 存入
        if line[-1] == 0:
            d[str(line[1])+'-'+str(line[2])] = 0
        if d.get(str(line[1])+'-'+str(line[2]), -1) == -1:
            # 说明还没有这个映射
            d[str(line[1])+'-'+str(line[2])] = line[-1]
        else:
            d[str(line[1])+'-'+str(line[2])] += line[-1]
    else:
        print(d[str(line[1])+'-'+str(line[2])])
