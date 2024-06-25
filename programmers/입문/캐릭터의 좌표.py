# 내 풀이 ( 테스트 통과, 정확성 45.5 )
# 이동 전 경계를 확인하고 이동 여부 결정
def solution1(keyinput, board):
    pos = [0, 0]
    move = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    for i in keyinput:
        if abs(pos[0]) >= (abs(board[0]) // 2) or abs(pos[1]) >= (abs(board[1]) // 2):
            continue
        else:
            if i == 'up':
                pos[0] += move[0][0]
                pos[1] += move[0][1]
            elif i == 'down':
                pos[0] += move[1][0]
                pos[1] += move[1][1]
            elif i == 'left':
                pos[0] += move[2][0]
                pos[1] += move[2][1]
            elif i == 'right':
                pos[0] += move[3][0]
                pos[1] += move[3][1]
    return pos



# 다른 풀이
# 이동 후 경계를 확인하고 이동 여부 결정
def solution2(keyinput, board):
    pos = [0, 0]
    move = {'up': [0, 1], 'down': [0, -1], 'left': [-1, 0], 'right': [1, 0]}
    x = board[0]//2
    y = board[1]//2
    for i in keyinput:
        new_x = pos[0] + move[i][0]
        new_y = pos[1] + move[i][1]
        if -x <= new_x <= x and -y <= new_y <= y:
            # 새로 옮긴 좌표가 범위 내의 수라면, pos에 적용
            pos[0] = new_x
            pos[1] = new_y
    return pos



# 테스트 케이스
print(solution1(["down", "down", "down", "down", "down", "down", "down", "down", "down"], [7, 9]))
print(solution1(["up", "up", "up", "up", "up", "up", "up", "up", "up"], [5, 5]))
print(solution1(["right", "right", "right", "right", "right", "right", "right", "right", "right"], [3, 3]))
print(solution1(["left", "left", "left", "left", "left", "left", "left", "left", "left"], [3, 3]))

