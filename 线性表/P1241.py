# P1241 括号序列
# 一开始写了很多，但是错了
# 发现按题意模拟即可

s = input()
# 是否匹配
vis = [0 for _ in range(len(s))]

for i in range(len(s)):
    if s[i] == ')' or s[i] == ']':
        for j in range(i, -1, -1):
            # 如果是左括号且未匹配
            if (s[j] == '(' or s[j] == '[') and vis[j] == 0:
                if s[i] == ')' and s[j] == '(':
                    vis[i] = 1
                    vis[j] = 1
                if s[i] == ']' and s[j] == '[':
                    vis[i] = 1
                    vis[j] = 1
                break

for i in range(len(s)):
    if vis[i] == 1:
        print(s[i], end='')
    else:
        if s[i] == '(' or s[i] == ')':
            print('(', end='')
            print(')', end='')
        elif s[i] == '[' or s[i] == ']':
            print('[', end='')
            print(']', end='')

'''
理解错题意的写法~
stack1 = []
stack2 = []

s = input()

stack1.append(s[0])

for i in range(1, len(s)):
    # 如果是右括号，则直接压入栈1
    if s[i] == '(' or s[i] == '[':
        stack1.append(s[i])
    else:
        # 如果是左括号，则判断是否与栈1的栈头匹配
        # 如果匹配，那就弹出栈头，压入栈2
        if stack1[-1] == '(' and s[i] == ')':
            stack1.pop()
            stack2.append('(')
            stack2.append(')')
        elif stack1[-1] == '[' and s[i] == ']':
            stack1.pop()
            stack2.append('(')
            stack2.append(')')
        # 如果不匹配，那么说明栈头是不完整的，那么就给栈头补一个
        elif s[i] == ')':
            while stack1[-1] != '(':
                t = stack1.pop()
                stack2.append('[')
                stack2.append(']')
            stack1.pop()
            stack2.append('(')
            stack2.append(')')
        else:
            while stack1[-1] != ']':
                t = stack1.pop()
                stack2.append('(')
                stack2.append(')')
            stack1.pop()
            stack2.append('[')
            stack2.append(']')

while len(stack1) > 0:
    if stack1[-1] == '(':
        stack1.pop()
        stack2.append('(')
        stack2.append(')')
    else:
        stack1.pop()
        stack2.append('[')
        stack2.append(']')
for item in stack2:
    print(item, end='')
'''
