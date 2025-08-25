grid = [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 1]
]
n, m = len(grid), len(grid[0])
visited = [[False] * m for _ in range(n)]

# 상,하,좌,우 탐색용 방향 벡터
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    # 1) 범위 밖이면 리턴
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    # 2) 이미 방문했거나 물(0)이면 리턴
    if visited[x][y] or grid[x][y] == 0:
        return 0

    visited[x][y] = True  # 3) 현재 칸 방문 처리
    size = 1  # 4) 현재 칸도 크기 1로 세기

    # 5) 상하좌우로 이어진 땅 재귀 호출
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        size += dfs(nx, ny)

    return size


print("DFS로 찾은 영역 크기:", dfs(0, 0))
