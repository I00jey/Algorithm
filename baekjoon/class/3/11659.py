# 구간 합 구하기 4

# n, m = map(int, input().split())
#
# numbers = list(map(int, input().split()))
#
# for _ in range(m):
#     i, j = map(int, input().split())
#     print(sum(numbers[i-1:j]))

# 시간 초과
# -------------------------------------------

# 빠른 입력
# input 대신 sys.stdin.readline이 더 빠르게 입력 처리
import sys
input = sys.stdin.readline

# 수 개수, 합을 구해야하는 횟수 입력
n, m = map(int, input().split())

# 수 입력
numbers = list(map(int, input().split()))
# 1번 인덱스부터 해당 인덱스까지의 합을 저장할 배열
sums = [0] * (n+1)
# 배열에 1번 인덱스부터의 합 저장
for k in range(1, n+1):
    sums[k] = sums[k-1] + numbers[k-1]
# 이 과정에서 sum() 함수를 쓰면 시간초과
# 그래서 앞 인덱스에 현재 수만 더하는 방식

# 합을 구하는 반복문
for _ in range(m):
    # 합을 구할 구간 입력받기
    i, j = map(int, input().split())
    # 미리 합을 구한 배열에서 j 인덱스에서 i-1 인덱스를 빼면 i-j 구간의 합이 나옴
    print(sums[j] - sums[i-1])
