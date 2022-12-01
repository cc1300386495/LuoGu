#  [NOIP2015 普及组] 扫雷游戏

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    line = input()
    matrix.append(line)


def check(i, j):
    if matrix[i][j] == '*':
        return '*'
    else:
        cnt = 0
        # 右、左、下、上、右上、右下、左上、左下
        for row, col in [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, 1], [1, 1], [-1, -1], [1, -1]]:
            if -1 < i + row < n and -1 < j + col < m:
                if matrix[i+row][j+col] == '*':
                    cnt += 1
        return str(cnt)


for i in range(n):
    for j in range(m):
        print(check(i, j), end='')
    print()
