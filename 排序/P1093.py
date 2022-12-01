# P1093 [NOIP2007 普及组] 奖学金
# 直接排序有一个问题，总分和语文成绩是从大到小排，但学号要求从小到大
# 因此需要对学号临时处理一下（取相反数，这样就等价于从小到大了），然后再排序输出即可

n = int(input())
records = []
for i in range(n):
    score = list(map(int, input().split()))
    stu = [sum(score), score[0], -(i+1)]  # 总分，语文成绩，学号
    records.append(stu)

records.sort(reverse=True)

for i in range(5):
    print(-records[i][2], records[i][0], sep=' ')
