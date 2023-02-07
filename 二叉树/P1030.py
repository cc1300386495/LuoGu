# P1030 [NOIP2001 普及组] 求先序排列
# 递归求解即可

front = input().strip()
tail = input().strip()


def findFront(front, tail):
    if len(front) > 0:
        print(tail[-1], end='')
        loc = front.find(tail[-1])
        left_front = front[:loc]
        left_tail = tail[:loc]
        right_front = front[loc+1:]
        right_tail = tail[loc:-1]
        findFront(left_front, left_tail)
        findFront(right_front, right_tail)


findFront(front, tail)
