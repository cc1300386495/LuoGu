# P1019 [NOIP2000 提高组] 单词接龙
# 先枚举出任意两个单词接龙后的长度，然后进行深搜

n = int(input().strip())

# 存储单词
words = []
for _ in range(n):
    words.append(input().strip())

# 记录每个单词的使用次数
used = [0 for _ in range(n)]

# 记录任意两个单词连接的重叠部分的长度
linkLength = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        leftWords = words[i]
        rightWords = words[j]
        temp = 0
        # 记录leftWords后面的字母与rightWords前面字母相等的个数
        for k in range(1, min(len(leftWords), len(rightWords)+1)):
            if leftWords[-k:] == rightWords[:k]:
                linkLength[i][j] = k
                break

# 记录最大的长度

res = 0

# 深度搜索


def dfs(i, length):
    global used, res
    # s表示当前字符串末尾连接的是哪个单词
    # length表示当前长度
    # 更新长度
    res = max(length, res)
    # 尝试接力每一个单词
    for j in range(n):
        # 如果没用到两次
        if used[j] < 2 and linkLength[i][j] != 0:
            # 连接后的长度
            t = length + len(words[j]) - linkLength[i][j]
            used[j] += 1
            dfs(j, t)
            used[j] -= 1


# 获取龙头
head = input().strip()

for i in range(n):
    if words[i][0] == head:
        used[i] += 1
        dfs(i, len(words[i]))
        used[i] -= 1
print(res)
