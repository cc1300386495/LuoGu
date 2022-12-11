# P1010 [NOIP1998 普及组] 幂次方
# 定义一个转换成二进制并打印的函数，递归调用即可

n = int(input())


def subStrIndex(substr, str):
    # 查找字符串中所有子串的下标
    result = []
    index = 0
    while str.find(substr, index, len(str)) != -1:
        temIndex = str.find(substr, index, len(str))
        result.append(temIndex)
        index = temIndex + 1
    return result


def toB(n):
    if n == 1:
        return '2'
    if n == 0:
        return '0'
    s = bin(n)[2:] + ''
    s = s[::-1]  # 二进制的1对应成下标
    loc = subStrIndex('1', s)[::-1]
    s = ''
    for i in range(len(loc)):
        if loc[i] == 1:
            s += '2'
        else:
            s += '2('
            s += toB(loc[i])
            s += ')'
        if i < len(loc) - 1:
            s += '+'
    return s


print(toB(n))
