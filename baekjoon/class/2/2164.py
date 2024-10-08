# 카드2

# 카드 개수
# n = int(input())
# cards = [0 for _ in range(n)]
#
# for i in range(n):
#     cards[i] = i+1
#
# while True:
#     if len(cards) == 1:
#         print(cards[0])
#         break
#
#     del cards[0]
#     cards.append(cards[0])
#     del cards[0]
#     # print(cards)


# 시간 초과
# del cards[0] 리스트의 첫번째 요소를 제거하고 모든 요소를 앞으로 한칸씩 이동
# => 시간 복잡도 O(n)
# del을 반복하면 시간 복잡도 O(n^2)

# ---------------------------------
# 풀이 2
# 리스트 대신 큐 queue 사용

from collections import deque

n = int(input())
# 1부터 n까지의 숫자를 deque에 저장
cards = deque(range(1, n+1))

# 큐의 길이가 1이 될 때까지 반복
while len(cards) > 1:
    # 첫번째 카드 버림
    cards.popleft()
    # 그 다음 카드를 큐 맨 뒤로 이동
    cards.append(cards.popleft())

# 마지막 남은 카드 출력
print(cards[0])


# ------------------------------------
# deque 정의
# 파이썬의 collections 모듈에서 제공하는 양방향 큐 double-ended queue
# 양쪽 끝에서의 삽입과 삭제가 매우 빠름
# deque에서 삽입&삭제시 시간 복잡도 => O(1)

# --------

# deque 주요 메서드
# collections.deque([iterable[, maxlen]])
# iterable = 초기화할 때 넣을 반복 가능한 객체
# maxlen = deque의 최대 길이 설정 (deque가 이 길이를 초과하면 자동으로 가장 오래된 항목 삭제)

# append(x)
# 오른쪽 끝에 요소 x 추가

# appendleft(x)
# 왼쪽 끝에 요소 x 추가

# pop()
# 오른쪽 끝에서 요소를 제거하고 반환

# popleft()
# 왼쪽 끝에서 요소를 제거하고 반환

# extend(iterable)
# 반복 가능한 객체의 요소들을 오른쪽 끝에 추가
# 시간 복잡도 => 추가하는 요소 수에 따라 O(k)

# extendleft(iterable)
# 반복 가능한 객체의 요소들을 왼쪽 끝에 추가
# 🚨 iterable 순서의 역순으로 추가됨

# rotate(n)
# deque를 회전
# n > 0이면, 오른쪽으로 n만큼 회전
# n < 0이면, 왼쪽으로 n만큼 회전
