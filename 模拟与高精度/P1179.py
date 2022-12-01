# P1179 [NOIP2010 普及组] 数字统计

l, r = map(int, input().split())
ans = 0
for i in range(l, r + 1):
    while i:
        if i % 10 == 2:
            ans += 1
        i = i // 10
print(ans)
