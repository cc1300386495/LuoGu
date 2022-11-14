# P2615 [NOIP2015 提高组] 神奇的幻方

n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
matrix[0][n // 2] = 1
last = [0, n // 2]  # 记录K-1的位置
for i in range(2, n*n + 1):
    if last[0] == 0 and last[1] != n-1:  # 满足条件1
        row = n-1  # 最后一行
        col = last[1] + 1  # k-1所在列的右一列
    elif last[0] != 0 and last[1] == n-1:
        row = last[0] - 1
        col = 0
    elif last[0] == 0 and last[1] == n-1:
        row = last[0] + 1
        col = last[1]
    elif last[0] != 0 and last[1] != n-1:
        if matrix[last[0] - 1][last[1] + 1] == 0:
            row = last[0] - 1
            col = last[1] + 1
        else:
            row = last[0] + 1
            col = last[1]
    matrix[row][col] = i
    last = [row, col]
for row in matrix:
    for i in row:
        print(i, end=" ")
    print()
