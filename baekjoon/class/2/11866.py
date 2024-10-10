import sys
from collections import deque
input = sys.stdin.readline

# 1-n번까지, k번째
n, k = map(int, input().split())
# 1-n까지 큐 초기화
queue = deque(range(1, n+1))
result = []

while len(queue) > 0:
    # rotate(x)
    # 큐가 x번만큼 회전
    # x가 양수이면, 첫번째 요소가 x+1번째 요소가 됨
    # x가 음수이면, 첫번째 요소가 뒤로 -x만큼 감

    # 번호가 1부터 시작하니까 +1
    # k번째 사람을 큐의 맨 앞으로 이동
    queue.rotate(-k+1)
    # print(queue)
    result.append(queue.popleft())

print('<'+ ', '.join([str(i) for i in result])+'>')