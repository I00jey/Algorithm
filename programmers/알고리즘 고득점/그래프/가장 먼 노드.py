from collections import deque
# 인접 행렬 사용
def bfs(node, visit, lis):
    que = deque()
    que.append(node)
    visit[node] = 1

    while que:
        top = que.popleft()

        for i in range(1, n+1):
            if lis[top][i] == 1 and visit[i] == 0:
                visit[i] = visit[top] + 1
                que.append(i)

    return


def solution(n, edge):
    answer = 0
    lis = [[0]*(n+1) for _ in range(n+1)]
    visit = [0] * (n+1)     # visit = [0,1,0,2,3]

    for e in edge:
        a, b = e[0], e[1]
        lis[a][b] = lis[b][a] = 1

    bfs(1, visit, lis)

    # print(visit)
    answer = visit[1:].count(max(visit[1:]))
    return answer

n = 6
edge = 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))