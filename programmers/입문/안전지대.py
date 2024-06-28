# 내 풀이
def solution(board):
    dangerous = []
    size = len(board) * len(board[0])
    movement = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                if [i,j] not in dangerous:
                    dangerous.append([i, j])
                for move in movement:
                    if 0 <= i + move[0] < len(board) and 0 <= j+move[1] < len(board) and [i + move[0], j + move[1]] not in dangerous:
                        dangerous.append([i + move[0], j + move[1]])
    return size - len(dangerous)


# 다른 풀이
def solution(board):
    # board의 크기 : n * n
    n = len(board)
    # danger은 집합 (중복된 위치를 자동으로 제거)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            # 현재 위치가 0이면 (위험하지 않을 지역이라면)
            if not x:
                # 현재 반복 건너뛰기
                continue
            # 현재 위치값이 1이라면, 그 위치와 주변 8개의 위치를 집합에 추가
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
            # (i+di,j+dj) : 현재 위치에서 각 방향으로 이동한 위치
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)
    # 전체 board 칸수 - (danger에 포함된 i, j 중 유효한 범위에 있는 위치의 개수)

