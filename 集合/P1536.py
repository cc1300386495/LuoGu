# P1536 村村通
# 如果所有的城镇都能相互连通，那么必然可以汇聚到同一个城市
# 也就是同一祖先，所有可以利用并查集的方法求解


def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]


while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1:
        break
    n, m = nums[0], nums[1]
    # 并查集部分
    p = [i for i in range(n+1)]
    # 不考虑0号城市
    p[0] = -1
    # 读取道路
    for i in range(m):
        r1, r2 = map(int, input().split())
        # 合并
        p[find(r1)] = find(r2)
    # 统计
    # 如果有城市不能汇聚到同一个中心城市，那么给他修路即可
    # 因为中心城市本身不需要修路，所以count初始化为-1
    count = -1
    for i in range(n+1):
        if p[i] == i:
            count += 1
    print(count)
