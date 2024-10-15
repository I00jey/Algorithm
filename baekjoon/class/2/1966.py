# 프린터 큐

# 내 풀이 (미완성)
from collections import deque

# testcase = int(input())
# for i in range(testcase):
#     n, m = map(int, input().split())
#     queue = deque(input().split())
#     # print(queue[m])
#     count = 0
#     while len(queue) > 0:
#         if m == 0 and max(queue) == queue[m]:
#             count += 1
#             break
#         else:
#             if queue[0] == max(queue):
#                 queue.popleft()
#                 count += 1
#             else:
#                 queue.append(queue.popleft())
#             m -= 1
#         print(queue)
#     print(count)

# --------------------------------------------------------
# 다른 풀이
# 테스트 케이스 수 입력
t = int(input())

for _ in range(t):
    # 문서의 개수, 인쇄 순서를 구할 문서의 현재 인덱스 입력받기
    n, m = map(int, input().split())
    # 문서 입력받기 (수의 크기가 문서 중요도에 비례)
    data = list(map(int, input().split()))

    # 인쇄 순서
    result = 1
    # 남은 문서가 없을 때까지 반복
    while data:
        # 첫번째 문서가 제일 중요한 문서가 아닐 경우
        if data[0] < max(data):
            # 첫번째 문서 제일 뒤로 보내기
            data.append(data.pop(0))

        # 첫번째 문서가 제일 중요한 문서일 경우
        else:
            # 첫번째 문서가 제일 중요한 문서이자, 인쇄순서를 구해야하는 문서일 경우
            if m == 0:
                # 반복문 종료
                break
            # 첫번째 문서 삭제
            data.pop(0)
            # 인쇄 순서 더하기
            result += 1

        # m이 0보다 크다면 인덱스 1씩 감소
        # m이 0이라면 리스트 가장 뒤로 이동
        m = m - 1 if m > 0 else len(data) - 1

    print(result)
