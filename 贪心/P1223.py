# P1223 排队接水
# 如果想让平均排队时间最短，那么让用时最短的人先排队即可

n = int(input())

# 记录每个人的接水时间及序号
record = []
line = list(map(int, input().split()))
for i in range(n):
    record.append([line[i], i])

record.sort(key=lambda x: x[0])
for item in record:
    print(item[1]+1, end=' ')

# 总等待时间
# 后面有多少人就乘以当前的接水时间 就是当前这个人制造的等待时间
all = sum([record[i][0] * (n-i-1) for i in range(n)])

# 输出
print()
print("%.2f" % (all/n))
