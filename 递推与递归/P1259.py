# P1259 黑白棋子的移动
# 题意读了半天才理解。大致意思就是想像有两个空位，也就是'--'
# 然后选择两个连续的（不区分颜色）与空位交换

# 解题思路
# n = 6 时，其子步骤必然包含n = 5的情况。
# 当n>=4时，规模为K的问题可以先将第K和第K+1个棋子移到最右边，再将第2K-1和2K个棋子移到K和K+1处
# 通过上述步骤，就可以转化为K-1的子问题。
# 完成分治

n = int(input())
s = 2 * n + 1
chess = [''] * 210  # 存放棋子


def init(n):
    # 初始化
    global chess
    for i in range(1, n+1):
        chess[i] = 'o'
    for i in range(n+1, 2*n+1):
        chess[i] = '*'
    for i in range(2*n+1, 2*n+3):
        chess[i] = '-'
    Print()


def Print():
    for i in range(1, 2*n+3):
        print(chess[i], end='')
    print()


def move(k):
    global chess, s
    for i in range(2):
        chess[s+i] = chess[k+i]
        chess[k+i] = '-'
    s = k
    Print()


def move1(n):
    if n == 4:
        move(4)
        move(8)
        move(2)
        move(7)
        move(1)
    else:
        move(n)
        move(2*n-1)
        move1(n-1)


init(n)
move1(n)
