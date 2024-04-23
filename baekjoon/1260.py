# 노드, 간선, 시작 노드 입력 받기
n, m, start = list(map(int,input().split(" ")))


# 그래프 간선 저장 리스트
lines = []
for _ in range(m):
    # 간선 수 만큼 간선 입력 받기
    lines.append(list(map(int, input().split(" "))))

nodes = []
for i in range(1, n+1):
    nodes.append(i)


# 깊이 우선 탐색 DFS
def deep_first():

    print()


# 너비 우선 탐색 BFS
def breadth_first():
    result = [start]
    for line in lines:
        if start in
    print(*result)


deep_first()
breadth_first()

