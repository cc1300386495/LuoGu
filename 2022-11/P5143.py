# P5143 攀爬者
# 先从低到高对点进行排序，然后计算距离即可

n = int(input())

dots = []

for _ in range(n):
    dots.append(list(map(int, input().split())))

dots.sort(key=lambda x: x[2])

dis = 0
for i in range(n-1):
    dis += ((dots[i][0] - dots[i+1][0])**2 + (dots[i][1] -
            dots[i+1][1])**2+(dots[i][2] - dots[i+1][2])**2)**0.5

print('%.3f' % dis)
