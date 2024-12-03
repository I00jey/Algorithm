# 1로 만들기

n = int(input())

# DP 테이블 초기화
d = [0] * 1000001

# 다이나믹 프로그래밍 진행 bottom-up
for i in range(2, n+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)

# 결과 출력
print(d[n])



# 코드 설명
# d[i] = i가 1이 되는데 필요한 연산의 최솟값
# 앞에 구한 결과값을 저장했다가 후에 사용
# 2와 3으로 나누어 떨어지지 않는 경우
# 무조건 1을 빼야 하기 때문에 dp[i] = dp[i-1] + 1을 통해 횟수를 +1
# 2 와 3으로 나누어 떨어지는 경우
# dp[i](1을 빼는 경우)와 dp[i//2or3]+1(나누었을 경우) 중 최소값을 선택