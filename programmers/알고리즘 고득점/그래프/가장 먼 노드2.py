from collections import deque
# 인접 행렬 사용
def bfs(node, visit, lis):
    que = deque()
    que.append(node)
    visit[node] = 1

    while que:
        top = que.popleft()

    return


def solution(n, edge):
    answer = 0
    lis = [[] for _ in range(n+1)]
    visit = [0] * (n+1)     # visit = [0,1,0,2,3]

    for e in edge:
        a, b = e[0], e[1]
        lis[a].append(b)
        lis[b].append(a)

    for i in lis:
        i.sort()

    print(lis)

    #bfs(1, visit, lis)

    # print(visit)
    answer = visit[1:].count(max(visit[1:]))
    return answer

n = 6
edge = 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))