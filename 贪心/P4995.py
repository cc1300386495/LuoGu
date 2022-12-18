# P4995 跳跳！
# 如果想要耗费尽可能多的体力值，那么就得保证每次跳的时候都得是当前消耗最大的一种。
# 也就是，在当前剩余的石头中从最高的跳到最矮的或者从最矮的跳到最高的

n = int(input())

height = [0] + list(map(int, input().split()))

res = 0

height.sort()

tag = True
left, right = 0, n
while left < right:
    res += (height[left] - height[right]) ** 2
    if tag:
        left += 1
        tag = False
    else:
        right -= 1
        tag = True

print(res)
