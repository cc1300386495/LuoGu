# P1177 【模板】快速排序

n = int(input())

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
    quick_sort(l, j)
    quick_sort(j+1, r)


quick_sort(0, n-1)
for i in range(n):
    print(nums[i], end=' ')
