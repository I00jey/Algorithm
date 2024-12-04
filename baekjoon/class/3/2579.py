# 계단 오르기

# -------------------------------------------------------
# 내 풀이

# 계단 수
n = int(input())
stairs = []
# 계단 입력받기
for i in range(n):
    stairs.append(int(input()))

# 계단 위에서부터 내려오기
stairs.reverse()
# print(stairs)

stairs.append(0)
score = stairs[0]
i = 0
while i <= n-2:
    score += max(stairs[i+1], stairs[i+2])
    if max(stairs[i+1], stairs[i+2]) == stairs[i+1]:
        i += 1
    else:
        i += 2

print(score)

# -------------------------------------------------------
# 다른 풀이
# 계단 수 입력
n = int(input())
# 계단 값 초기화
stairs = [0] * 301
# 계단 입력받기
for i in range(1, n+1):
    stairs[i] = int(input())

# dp 초기화 (= i단까지 올라가는데 점수의 최댓값)
dp = [0] * 301
# 1단까지의 최댓값 = 1번째 계단 점수
dp[1] = stairs[1]
# 2단까지의 최댓값 = 1번째 + 2번째 계단 점수
dp[2] = stairs[1] + stairs[2]
# 3단까지의 최댓값 = (1번째 + 3번째 계단 점수) or (2번째 + 3번째 계단 점수) 중 최댓값
dp[3] = max(stairs[1]+ stairs[3], stairs[2]+stairs[3])

# 반복문을 통해 4단부터 최댓값 구하기
for i in range(4, n+1):
    dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    # dp[i-3] + stairs[i-1] + stairs[i]
    # >> i-3 단을 밝고 순서대로 i-1, i단을 밟은 경우
    # dp[i-2] + stairs[i]
    # >> i-2 단까지 밟고 i-1을 뛰어넘고 바로 i단을 밟은 경우
    # 이 두가지 경우 중 점수의 최댓값을 해당 인덱스에 저장
print(dp[n])
