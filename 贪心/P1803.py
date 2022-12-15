# P1803 凌乱的yyy / 线段覆盖
# 区间合并问题
# 按右端点（结束时间）进行排序

n = int(input())

# 记录每场比赛开始和结束的时间
record = []
for _ in range(n):
    line = list(map(int, input().split()))
    record.append(line)

record.sort(key=lambda x: x[1])

count = 0
end = -1

for item in record:
    if end <= item[0]:
        count += 1
        end = item[1]

print(count)
