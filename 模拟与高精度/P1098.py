# P1098 [NOIP2007 提高组] 字符串的展开
# 难点在于 如何修改字符串
# 创造一个新字符串
# p1可能取值1,2,3 p3可能取值1,2
# 所以一共有6种组合方式

p1, p2, p3 = map(int, input().split())
s = input()
res = ''

for i in range(len(s)):
    if s[i] != '-':
        res += s[i]
    else:
        # 首位、末位、左边是数字右边是字母、连续多个"-"、右边是数字左边是字母——都原样输出即可
        if i == 0 or i == len(s) - 1 or s[i + 1] == "-" \
                or s[i - 1] == "-" or ("0" <= s[i - 1] <= "9" and "a" <= s[i + 1] <= "z") or ord(s[i - 1]) >= ord(s[i + 1]):
            res += s[i]  # 原样输出
            continue
        # 比较大小
        elif ord(s[i+1]) - ord(s[i-1]) == 1:
            continue
        else:
            temp = ''
            for j in range(1, ord(s[i+1]) - ord(s[i-1])):
                if p1 == 3:
                    temp += '*' * p2  # p2 是指重复个数
                else:  # 添加字母
                    temp += chr(ord(s[i-1]) + j) * p2
            if p1 == 2:
                temp = temp.upper()  # 转化为大写
            if p3 == 2:
                temp = temp[::-1]  # 逆序
            res += temp
print(res)
