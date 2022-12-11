# P3612 [USACO17JAN]Secret Cow Code S
# 先思考:如果只是单纯的重复，没有反转，那么就可以不断的递推。
# 所以，只需要特判一下即可

s, n = input().split()
n = int(n)
l = len(s)

# s[n]==s[n+1],s[1] 到 s[n-1] 依次与 s[n+2] 到 s[2n] 相等


def find(n):  # 找到第n个字符
    if n <= l:
        print(s[n-1])
        return
    i = l
    while i < n:
        # 找到总长度的一半
        i = i * 2
    i = i // 2
    n = n - i - 1
    if n == 0:
        n = i
    find(n)


find(n)
# 模拟 只过40分


# s, n = input().split()
# n = int(n)
# l = len(s)
# while l < n:
#     s = s + s[-1] + s[:l-1]
#     l = l + l
# print(s[n-1])
