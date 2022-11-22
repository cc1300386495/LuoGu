# P1068 [NOIP2009 普及组] 分数线划定

n, m = map(int, input().split())

persons = []

for i in range(n):
    input_line = list(map(int, input().split()))
    persons.append(input_line)

persons.sort(key=lambda x: [x[1], -x[0]], reverse=True)  # 先按成绩从大到小排，再按学号从小到大排

score = persons[int(m*1.5) - 1][1]  # 分数线

cnt = 0
while persons[cnt][1] >= score:
    cnt += 1

print(score, cnt, sep=' ')

for i in range(cnt):
    print(persons[i][0], persons[i][1], sep=' ')
