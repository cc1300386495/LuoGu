# P2240 【深基12.例1】部分背包问题
# 因为数据范围比较小
# 所以先求出每堆的单位价格，从单位价格最高的金币堆开始拿

N, T = map(int, input().split())

# 背包当前重量
weight = 0
# 背包当前价值
value = 0

record = []
# 读取每堆的价值和重量
for _ in range(N):
    line = list(map(int, input().split()))
    record.append(line)

# 按单位价值排序(升序)
record.sort(key=lambda x: x[1]/x[0], reverse=True)

# 先去单位价值最高的
i = 0
while weight < T:
    if T - weight > record[i][0]:
        weight += record[i][0]
        value += record[i][1]
        i += 1
    else:
        value += (T-weight) * (record[i][1]/record[i][0])
        break
    # 背包容量大于所以金币的总重量
    if i >= len(record):
        break
print("%.2f" % (value))
