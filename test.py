# 测试一些语法~
import re

s = '' + bin(10)[2:]
p = re.compile(r'1')

print(re.finditer(p, s))
res = s.find('1')
print(res)
