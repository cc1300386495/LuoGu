# P1160 队列安排
# 解法看注释

n = int(input())

# 第i个嵌套列表表示编号为i的同学左边和右边站的同学
students = [[-1, -1] for _ in range(n)]


def insertLeft(i, k):
    global students
    # 该函数用于将编号为i的同学，插入到编号为k的同学的左边
    # 先取出同学k左边的同学编号
    kLeft = students[k][0]
    # 然后将kLeft的右边改为第i个同学，同理第i个同学的左边改成kLeft
    students[kLeft][1] = i
    students[i][0] = kLeft
    # 按照同样的思路修改k
    students[k][0] = i
    students[i][1] = k
    # 如果上面的交换不懂，可以画图模拟一下


def insertRight(i, k):
    global students
    # 与insetLeft同理
    kRight = students[k][1]

    students[kRight][0] = i
    students[i][1] = kRight

    students[k][1] = i
    students[i][0] = k


for i in range(1, n):
    k, p = map(int, input().split())
    if p == 0:
        insertLeft(i, k-1)
    else:
        insertRight(i, k-1)

m = int(input())
for _ in range(m):
    move = int(input()) - 1
    if students[move][0] != -2:
        moveLeft, moveRight = students[move][0], students[move][1]
        students[moveLeft][1] = moveRight
        students[moveRight][0] = moveLeft
        students[move][0] = -2
        students[move][1] = -2
# 输出队列
# 先找到队头，也就是左边为-1的同学
for i in range(n):
    if students[i][0] == -1:
        head = i
        break
next = head
while next != -1:
    print(next + 1, end=' ')
    next = students[next][1]
