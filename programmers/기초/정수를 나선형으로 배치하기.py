# 내 풀이
def solution(n):
    answer = [[0]*n for _ in range(n)]
    x, y = 0, 0
    mode = "right"
    for i in range(n**2):
        answer[x][y] = i + 1
        if mode == "right":
            y += 1
            if y == n or answer[x][y] != 0:
                y -= 1
                mode = "down"
                x += 1
        elif mode == "down":
            x += 1
            if x == n or answer[x][y] != 0:
                x -= 1
                mode = "left"
                y -= 1
        elif mode == "left":
            y -= 1
            if y == -1 or answer[x][y] != 0:
                y += 1
                mode = "up"
                x -= 1
        elif mode == "up":
            x -= 1
            if x == -1 or answer[x][y] != 0:
                x += 1
                mode = "right"
                y += 1

    return answer

# 다른 풀이
def solution2(n):
    answer = [[0]*n for _ in range(n)]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x, y, mode = 0, 0, 0
    for i in range(1, n**2+1):
        answer[x][y] = i
        if y + move[mode][1] >= n or x + move[mode][0] >= n or answer[x + move[mode][0]][y + move[mode][1]]:
            mode = (mode + 1) % 4
        x, y = x+move[mode][0], y+move[mode][1]
    return answer

print(solution2(4))