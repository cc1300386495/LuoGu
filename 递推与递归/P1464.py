# P1464 Function
# 本题的难点在于，递归的层数会很多
# 所以我们可以采用记忆化，也就是在递归的过程中保存结果
# 由题意可知，只要任意a,b,c大于20，返回的都是w(20,20,20)
# 所以我们只要开一个三维数组存储结果即可

w = [[[None for _ in range(21)] for _ in range(21)] for _ in range(21)]


def f(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return f(20, 20, 20)
    if w[a][b][c] != None:
        return w[a][b][c]
    if a < b < c:
        w[a][b][c] = f(a, b, c-1) + f(a, b-1, c-1) - f(a, b-1, c)
    else:
        w[a][b][c] = f(a-1, b, c) + f(a-1, b-1, c) + \
            f(a-1, b, c-1) - f(a-1, b-1, c-1)
    return w[a][b][c]


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        print("w({}, {}, {}) = {}".format(a, b, c, f(a, b, c)))
