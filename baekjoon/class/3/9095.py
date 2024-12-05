# 1, 2, 3 더하기

# 내 풀이
t = int(input())

dp = [0] * 11
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7
for j in range(4, 11):
    dp[j] = dp[j-1] + dp[j-2] + dp[j-3]

for i in range(t):
    n = int(input())
    print(dp[n])



