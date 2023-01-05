# P3156 【深基15.例1】询问学号

# 此题Python卡的过眼，下面的代码只有20分
n, q = map(int, input().split())

students = list(map(int, input().split()))

querys = list(map(int, input().split()))

for i in querys:
    print(students[i-1])
