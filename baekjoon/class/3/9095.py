# 1, 2, 3 더하기

# 내 풀이
t = int(input())

dp = [0] * 11
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7

# 위 패턴으로 dp[4] = dp[3] + dp[2] + dp[1] 다음 식이 성립됨을 알수있음
# 더해서 4가 되는 경우
# 1) dp[3] '+ 1' = 1, 2, 3의 합으로 3가 되는 식 맨 뒤에 +1을 붙인 경우
# 2) dp[2] '+ 2' = 1, 2, 3의 합으로 2가 되는 식 맨 뒤에 +2을 붙인 경우
# 3) dp[1] '+ 3' = 1, 2, 3의 합으로 1가 되는 식 맨 뒤에 +3을 붙인 경우
# 위의 경우는 원래 있던 식 뒤에 +1 +2 +3만 붙였으므로 경우의 수는 dp[4] dp[3] dp[2]와 같다
# 즉, dp[4] = dp[3] + dp[2] + dp[1]  모든 경우의 수의 합

for j in range(4, 11):
    dp[j] = dp[j-1] + dp[j-2] + dp[j-3]

for i in range(t):
    n = int(input())
    print(dp[n])



