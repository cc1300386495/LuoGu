# P1271 【深基9.例1】选举学生会
# 常规方法：sort排序，然后输出
# 思路：桶排序
# 有任意一张选票都对应着1~n中的某一个数。因此，可以开一个长度为n的数组，维护i出现的次数(1<=i<=n)，然后按顺序输出即可

n, m = map(int, input().split())

records = [0 for i in range(n+1)]

input_list = list(map(int, input().split()))
for i in input_list:
    records[i] += 1  # 出现次数加1

start = 0  # 从头开始遍历

while start <= n:
    if records[start] == 0:  # 说明这个候选人的选票输出完了
        start += 1
        continue
    else:
        print(start, end=' ')
        records[start] -= 1
