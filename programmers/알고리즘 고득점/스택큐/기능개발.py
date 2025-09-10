import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    # 각 기능별 완료까지 남은 일수 계산
    days_needed = deque([math.ceil((100-p)/s) for p, s in zip(progresses, speeds)])
    # zip 함수 -> 여러 개의 iterable 객체들을 인자로 받아 각 객체에서 동일한 인덱스에 있는 요소들을 묶어서 튜플 (...)형태로 반환
    print('days_needed', days_needed)
    while days_needed:
        # 첫 번째 기능이 배포될 때까지 걸리는 일수
        current_day = days_needed.popleft()
        # 첫 번째 기능은 무조건 배포에 포함
        count = 1

        # 기능 완료까지 걸리는 일수가 current_day 이하인 기능을 찾아서 연속 제거
        while days_needed and days_needed[0] <= current_day:
            days_needed.popleft()
            count += 1

        answer.append(count)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))