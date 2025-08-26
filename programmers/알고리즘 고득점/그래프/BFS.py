from collections import deque

grid = [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 1]
]
n, m = len(grid), len(grid[0])
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    if grid[x][y] == 0:
        return 0

    q = deque()
    q.append((x, y))
    visited[x][y] = True
    size = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            # 1) 범위 체크
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 2) 땅이고 미방문이면
            if grid[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                size += 1
                q.append((nx, ny))
    return size


print("BFS로 찾은 영역 크기:", bfs(0, 0))
