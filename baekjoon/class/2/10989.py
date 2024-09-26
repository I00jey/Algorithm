# 내 풀이 ( 메모리 초과 )
# 제너레이터를 사용했지만
# sorted() 함수가 모든 값을 한번에 메모리로 로드해 정렬하기 때문에 제너레이터가 아닌 리스트로 변환
# n = int(input())
# numbers = sorted(int(input()) for _ in range(n))
#
# for num in numbers:
#     print(num)


# 메모리 초과 해결방법
# 1. 외부 정렬
# 2. 병합 정렬
# 3. 디스크 기반 정렬

# 입력을 한번에 받아서 쪼개기
# (실행 시간은 짧아졌지만 메모리 초과)
# import sys
# input = sys.stdin.read
#
# n = int(input().splitlines()[0])  # 첫 번째 줄의 숫자 개수
# numbers = sorted(map(int, input().splitlines()[1:n+1]))  # 나머지 입력을 모두 처리
#
# for num in numbers:
#     print(num)


# sorted, input() 사용 X
import sys
n = int(sys.stdin.readline())
# 인덱스가 10000까지
# 인덱스 => 입력 숫자
# 값 => 해당 숫자가 입력된 횟수
num_list = [0] * 10001


for _ in range(n):
    # 입력된 수의 개수만큼 반복
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    # n이 아니라 10001인 이유
    # n은 입력 숫자의 개수이고, 최댓값이 10,000,000
    # 입력된 수가 저장된 리스트 길이 => 10001
    if num_list[i] != 0:
        # 해당 인덱스(숫자)가 입력이 되었다면
        for _ in range(num_list[i]):
            # 입력된 횟수만큼 반복 출력
            print(i)