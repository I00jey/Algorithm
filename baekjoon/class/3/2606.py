# 바이러스

# 내 풀이
# from collections import deque
#
# # 컴퓨터의 수
# computer = int(input())
# # 연결 선의 수
# edge = int(input())
# edges = []
# for i in range(edge):
#     edges.append(list(map(int, input().split())))
#
# edges.sort()
# # print(edges)
#
# virus = []
# warms = deque()
# warms.appendleft(1)
#
# while warms:
#     # print(warms)
#     parent = warms.popleft()
#     for edge in edges:
#         if parent in edge:
#             other = [i for i in edge if i != parent]
#             # print('현재 edge', edge, '/ 현재 virus', other)
#             warms.append(other[0])
#             virus.append(other[0])
#             edges.remove(edge)
#
# virus = set(virus)
# virus = [i for i in virus if i != 1]
# print(len(virus))

# ---------------------------------------------------------------------
# 다른 풀이
from collections import deque

# 컴퓨터의 수
computer = int(input())
# 연결 선의 수
edge = int(input())

# 그래프 초기화
graph = {i: [] for i in range(1, computer+1)}
for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visitied = set()

# BFS 탐색
queue = deque([1])
while queue:
    current = queue.popleft()
    # 감염되지 않은(= 방문하지 않은) 컴퓨터일 경우
    if current not in visitied:
        # 감염된 컴퓨터 추가
        visitied.add(current)
        # 연결된 컴퓨터 추가
        queue.extend(graph[current])
    # print('현재까지 감염된 컴퓨터 : ', visitied)
    # print('현재 연결 컴퓨터 : ', queue)

# DFS 탐색
stack = [1] # 깊이우선탐색은 스택 사용
while stack:
    current = stack.pop()
    # 감염되지 않은 컴퓨터일 경우
    if current not in visitied:
        # 감염된 컴퓨터 추가
        visitied.add(current)
        # 감염된 컴퓨터와 연결된 컴퓨터들을 스택에 추가
        stack.extend(graph[current])


# 1을 제외한 감염된 컴퓨터의 수
print(len(visitied)-1)

