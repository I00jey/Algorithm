# 듣보잡

import sys

n, m = map(int, sys.stdin.readline().strip().split())

name_dict = {}
result = []

for i in range(n):
    name = sys.stdin.readline().strip()
    if name in name_dict.keys():
        name_dict[name] += 1
    else:
        name_dict[name] = 1

for i in range(m):
    name = sys.stdin.readline().strip()
    if name in name_dict.keys():
        result.append(name)
    else:
        continue

result.sort()
print(len(result))
for i in result:
    print(i)


