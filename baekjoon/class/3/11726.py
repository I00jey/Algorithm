# 2×n 타일링

d = [0] * 1001
# 1
d[1] = 1
# 2 = 1 + 1 = 2
d[2] = 2
# 3 = 1 + 1 + 1 = 2 + 1 = 1 + 2
d[3] = 3
# 4 = 1 + 1 + 1 + 1 = 1 + 1 + 2 = 2 + 1 + 1 = 1 + 2 + 1 = 2 + 2
# d[3] + 1
# d[2] + 2
d[4] = 5

for i in range(4, 1001):
    d[i] = d[i-2] + d[i-1]
n = int(input())
print(d[n] % 10007)