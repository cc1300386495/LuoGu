# P1229 遍历问题
# 首先，由定义可知：
# 只有一个儿子节点的节点才会满足前后遍历相同但子树不同
# 且子树只有两种选择，所有找出只有一个儿子节点的个数n,ans = 2 ** n

# 前序
lr = input().strip()
# 后序
rl = input().strip()

ans = 0
for i in range(len(lr)):
    for j in range(1, len(rl)):
        if lr[i] == rl[j]:
            if i + 1 < len(lr) and j - 1 > -1 and lr[i+1] == rl[j-1]:
                ans += 1
print(1 << ans)
