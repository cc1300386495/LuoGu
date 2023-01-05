# P1449 后缀表达式
# 遇到数字就压入，遇到运算符就计算，然后结果在压入

s = input()

t = ''

nums = []
for i in range(len(s)):
    if '0' <= s[i] <= '9':
        t += s[i]
    if s[i] == '.':
        nums.append(int(t))
        t = ''
    if s[i] == '+':
        n1 = nums.pop()
        n2 = nums.pop()
        nums.append(n1+n2)
    if s[i] == '-':
        n1 = nums.pop()
        n2 = nums.pop()
        nums.append(n2-n1)
    if s[i] == '*':
        n1 = nums.pop()
        n2 = nums.pop()
        nums.append(n1*n2)
    if s[i] == '/':
        n1 = nums.pop()
        n2 = nums.pop()
        nums.append(n2//n1)
    if s[i] == '@':
        print(nums[0])
        break
