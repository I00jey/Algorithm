# 랜선 자르기
import sys
input = sys.stdin.readline

# 현재 랜선 개수, 목표 랜선 개수
k, n = map(int, input().split())

# 현재 랜선 길이 저장 리스트
numbers = []
for _ in range(k):
    numbers.append(int(input()))

# 최종 결과를 저장할 변수
result = 0

# 범위 시작, 끝 변수
left = 1
right = max(numbers)

# 이분 탐색
while left <= right:
    mid = (left + right) // 2
    # count 초기화
    count = 0

    for num in numbers:
        count += num // mid

    # 원하는 랜선 개수보다 많거나 같은 경우
    if count >= n:
        # 현재 mid 값을 결과로 저장
        result = mid
        # 더 긴 랜선 길이를 찾기 위해 범위를 오른쪽으로 이동
        left = mid + 1
    else:
        # 랜선 개수가 부족한 경우 범위를 왼쪽으로 이동
        right = mid - 1

print(result)
