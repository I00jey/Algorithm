# 동전 0

import sys
n, k = map(int, sys.stdin.readline().strip().split())

coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline().strip()))

reversed_coins = sorted(coins, reverse=True)
count = 0

for coin in reversed_coins:
    if k >= coin:
        count += k // coin
        k = k % coin

print(count)