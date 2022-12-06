# P1928 外星密码
# 递归

s = input()
index = 0


def dfs():
    global index
    res = ''  # 存储解压出的字符串
    times = ''  # 存储需要重复的次数
    while index < len(s):
        if s[index] == '[':
            index += 1
            res += dfs()
        elif s[index].isnumeric():
            times += s[index]
            index += 1
        elif s[index] == ']':
            index += 1
            return res * int(times)
        else:
            res += s[index]
            index += 1
    return res


print(dfs())
# 下面的代码是非递归的思路，但只能过部分样例
# 貌似是在重复字符串处理那里出了问题，可以考虑额外维护一个栈
# 可以按照求解表达式的方法，维护一个栈

# s = input()
# n_s = ''  # 存储答案
# temp = ''  # 记录需要重复的字符串
# times = ''  # 存储重复次数
# save = [] # 存储每个解压内的字符串
# stack = []
# for i in range(len(s)):
#     if s[i] == '[':  # 解压
#         stack.append(s[i])
#     elif s[i] == ']':  # 解压结束，处理重复字符串
#         while True:
#             t = stack.pop()
#             if t == '[':
#                 times = times[::-1]
#                 times = int(times)
#                 if stack:
#                     temp = temp * times
#                 else:
#                     n_s += temp * times
#                 times = ''
#                 break
#             else:
#                 times += t
#     elif not stack:  # 栈为空
#         n_s += s[i]
#     elif s[i].isnumeric():
#         stack += s[i]
#     else:
#         temp += s[i]

# print(n_s)
