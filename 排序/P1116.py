# P1116 车厢重组
# 冒泡排序即可，每交换一次，次数加1，直至排序完成。

n = int(input())

# 看讨论发现这道题的输入有问题（可能不止2行），不能用下面这行代码处理
# trains = list(map(int, input().split()))

trains = []
while len(trains) < n:
    trains += [int(i) for i in input().split()]

cnt = 0  # 统计次数
for i in range(n):
    # 内循环每次将最大值放在最右边
    for j in range(n-1-i):
        if trains[j] > trains[j+1]:
            trains[j], trains[j+1] = trains[j+1], trains[j]
            cnt += 1
print(cnt)
