from collections import deque

def dfs(start):     # 재귀
    print(start, end=" ")
    visit[start] = 1

    for i in range(1, n+1):
        if arr[i][start] == 1 and not visit[i]:
            dfs(i)

    return

def bfs(start):     # queue
    que = deque()
    que.append(start)
    visit[start] = 1

    print(start, end=" ")

    while que:
        top = que.popleft()

        for i in range(1, n+1):
            if not visit[i] and arr[i][top] == 1:
                que.append(i)
                visit[i] = 1
                print(i, end=" ")

    return

n, m, v = map(int, input().split(" "))
visit = [0 for _ in range(n+1)]  # 노드 방문 기록 -> [0,1,1,0]
arr = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split(" "))
    arr[a][b] = arr[b][a] = 1

dfs(v)
print()
visit = [0 for _ in range(n+1)]  # 노드 방문 기록 -> [0,1,1,0]
bfs(v)