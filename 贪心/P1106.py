# P1106 删数问题
# 具体思路见代码

# 按字符串读入
n = input().strip()

k = int(input())

# 查看最后需要保留几位
keep = len(n) - k

res = ''

i = 0
t = 0
# 保证最高位的值最小
while keep > 0:
    temp = 10
    # 只要后面的数够删，就往后找
    while t <= len(n) - keep:
        if int(n[t]) < temp:
            temp = int(n[t])
            i = t
        t += 1
    keep -= 1
    res += n[i]
    t = i + 1
print(int(res))
