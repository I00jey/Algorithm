# Four Squares

import sys

n = int(sys.stdin.readline())
# dp[idx] -> idx라는 수를 만드는데 필요한 수의 개수 (최소값)
dp = []

# dp 리스트에 제곱수들을 저장
# 입력값이 제곱수라면 필요한 수의 개수 -> 1
k = 1
while k ** 2 <= n:
    dp[k**2] = 1
    k += 1

for i in range()

