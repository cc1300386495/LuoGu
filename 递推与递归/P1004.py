# P1044 [NOIP2003 普及组] 栈
# 设f[i]表示i个数的可能数量
# 假设x表示最后一个出栈的，那么可以将1~n分为2部分
# 大于x和小于x的
# 大于x的可能为f[n-x],小于x的可能为f[x-1]
# 所以x的总的可能性为：f[n-x] * f[x-1]

n = int(input())

f = [0 for _ in range(n+10)]
f[0] = 1
f[1] = 1
res = f[1]
for x in range(2, n+1):
    # x可能取值为1~n
    for j in range(x):
        f[x] += f[j] * f[x-j-1]
print(f[n])
