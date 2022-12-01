# P1518 [USACO2.4]两只塔姆沃斯牛 The Tamworth Two
# 本题难点：如何判断不能抓到？
# 解决方法：设置一个阈值  因为10*10的方格，四个方向，所以走不了太多次~
# 另外注意：转弯也需要1分钟，步数不改变

# 读入地图，顺便记录F和C的起始位置

maps = []
for i in range(10):
    line = input()
    for j in range(10):
        if line[j] == 'C':
            c_loc = [i, j]
        if line[j] == 'F':
            f_loc = [i, j]
    maps.append(line)

dirc = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# 初始向北移动
t_c = 0  # 方向改变的次数
t_f = 0  # 同上


def move_c():
    global t_c
    move = dirc[t_c % 4]  # 此时应该往哪个方向移动
    if c_loc[0] + move[0] < 0 or c_loc[0] + move[0] > 9 or c_loc[1] + move[1] < 0 or c_loc[1] + move[1] > 9:  # 越界
        t_c += 1  # 转变方向
    elif maps[c_loc[0] + move[0]][c_loc[1] + move[1]] == '*':  # 下一步是障碍
        t_c += 1  # 转变方向
    else:
        c_loc[0] += move[0]
        c_loc[1] += move[1]


def move_f():
    global t_f
    move = dirc[t_f % 4]  # 此时应该往哪个方向移动
    if f_loc[0] + move[0] < 0 or f_loc[0] + move[0] > 9 or f_loc[1] + move[1] < 0 or f_loc[1] + move[1] > 9:  # 越界
        t_f += 1  # 转变方向
    elif maps[f_loc[0] + move[0]][f_loc[1] + move[1]] == '*':  # 下一步是障碍
        t_f += 1  # 转变方向
    else:
        f_loc[0] += move[0]
        f_loc[1] += move[1]


t = 0
tag = True
while t < 16000:  # 设置阈值
    move_c()
    move_f()
    t += 1
    if c_loc[0] == f_loc[0] and c_loc[1] == f_loc[1]:
        tag = False
        print(t)
        break

if tag:  # 16000次都没抓住，肯定抓不住
    print(0)
