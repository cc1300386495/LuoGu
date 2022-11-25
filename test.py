# 测试一些语法~

import time
import math

start = time.time()
for i in range(10000):
    math.factorial(10000)
end = time.time()
print(end - start)
