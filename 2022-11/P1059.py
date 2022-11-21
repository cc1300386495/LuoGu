# 桶排序
# 详细介绍请看P1271

n = int(input())
cnt = 0
records = [0 for i in range(1000 + 1)]
input_list = list(map(int, input().split()))

for item in input_list:
    if records[item] == 0:
        cnt += 1
    records[item] += 1

print(cnt)
for i in range(1000+1):
    if records[i] == 0:
        continue
    else:
        print(i, end=' ')
