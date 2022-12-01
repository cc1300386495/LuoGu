# P1923 【深基9.例4】求第 k 小的数
# 思路:显然与排序有关。在快排过程中，我们不断划分数组，对子数组排序。在递归过程中，左数组是一定小于右数组的
# 因此，我们只需要对包含k的数组进行递归即可。其他数组无需在意。

n, k = map(int, input().split())

nums = list(map(int, input().split()))


def quick_sort(l, r):
    global nums
    if l >= r:
        return
    i = l - 1
    j = r + 1
    x = nums[(i + j)//2]
    while i < j:
        while True:
            i += 1
            if nums[i] >= x:
                break
        while True:
            j -= 1
            if nums[j] <= x:
                break
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    # 原来的快排需要对两边都进行排序
    # quick_sort(l, j)
    # quick_sort(j+1, r)
    # 现在只需要对包含k的数组排序即可
    if k <= j:
        quick_sort(l, j)
    else:
        quick_sort(j+1, r)


quick_sort(0, n-1)
print(nums[k])

# 上述代码后两个样例MLE，但在其他OJ平台提交无误。
# 附上能通过洛谷的代码
# import numpy as np

# n, k = map(int, input().split())
# arr = np.fromstring(input(), dtype = np.uint32, sep=' ')
# arr.sort()
# print(arr[k])
