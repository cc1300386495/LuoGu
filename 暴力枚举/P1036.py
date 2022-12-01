# P1036 [NOIP2002 普及组] 选数
# 继续深度遍历搜素，对于每个数只有两种情况，选与不选
# 只要当选择的数量等于k时，判断即可

def isPrime(i):
    for j in range(2, int(i ** 0.5 + 1)):
        if i % j == 0:
            return False
    return True


n, k = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
temp = []  # 用于存储选择的数


def dfs(i, t):  # 选到了下标为i的数，选择的数量为t个
    global cnt
    global temp
    if t == k:
        if isPrime(sum(temp)):
            cnt += 1
            return
    if i >= n:
        return
    # 选择这个数
    temp.append(nums[i])
    dfs(i+1, t+1)
    # 回溯，且不选择这个数
    temp.pop()
    dfs(i+1, t)


dfs(0, 0)
print(cnt)
