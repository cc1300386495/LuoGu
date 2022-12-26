# P1873 [COCI 2011/2012 #5] EKO / 砍树

# 妙计
n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 先排序
trees.sort()

sum = 0
# 从第left棵树砍到最后一个，先从最后一个开始砍
left = n - 1
while sum < m:
    # 从left - 1到最后一棵树，每棵树都要再减去left-1，left 的高度差
    sum += (trees[left] - trees[left-1]) * (n - left)
    left -= 1
# 当循环结束时，sum一定大于m，所以多出来的那部分，就可以使得已经砍掉的树少砍一些
left += 1

ans = trees[left-1]+(sum-m)/(n-left)

print(int(ans))

# 二分（70分，TLE）
# n, m = map(int, input().split())
# trees = list(map(int, input().split()))

# # 最低树、最高树
# low = 0
# height = max(trees)

# while low < height:
#     mid = (low + height + 1) // 2
#     s = 0
#     for i in range(n):
#         if (trees[i] > mid):
#             s += trees[i] - mid
#     if s < m:
#         height = mid - 1
#     else:
#         low = mid
# print(low)
