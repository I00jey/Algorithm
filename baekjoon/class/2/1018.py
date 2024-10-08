# 체스판 다시 칠하기
# 내 풀이 (오답)

# # 체스판 크기 입력
# n, m = map(int, input().split())
# # 체스판 초기화
# chess = [['0' for _ in range(m)] for _ in range(n)]
#
# # 체스판 입력받기
# for i in range(n):
#     string = input()
#     for j in range(m):
#         chess[i][j] = string[j]
#     # print(' '.join(chess[i]))
#
#
# # 8x8 크기로 자를 때 왼쪽 맨위 가능 좌표
# chess_start_list = []
#
# for i in range(n-8+1):
#     for j in range(m-8+1):
#         chess_start_list.append([i, j])
#
# # print(chess_start_list)
#
#
#
# # 체스판을 다시 칠한 횟수
# count = 0
# # 체스판을 다시 칠한 횟수 배열
# count_lis = []
#
# for x, y in chess_start_list:
#     print(x, y, "~", x+7, y+7)
#     for i in range(x, x+8):
#         if i < x + 7:
#             if chess[i][0] == chess[i+1][0]:
#                 count += 1
#                 print(i+1, 0)
#                 if chess[i][0] == 'W':
#                     chess[i+1][0] = 'B'
#                 else:
#                     chess[i+1][0] = 'W'
#         for j in range(y, y+7):
#             front = chess[i][j]
#             back = chess[i][j+1]
#             if front == back:
#                 print(i, j+1)
#                 count += 1
#                 if front == 'W':
#                     chess[i][j+1] = 'B'
#                 else:
#                     chess[i][j+1] = 'W'
#     print(count)
#     count_lis.append(count)
#     count = 0
#
#
# print(min(count_lis))



# ----------------------------------------------------
# 다른 풀이

# 체스판 크기 입력
n, m = map(int, input().split())
# 체스판
board = []
# 새로 칠한 체스판 개수 리스트
result = []

# 체스판 입력
for _ in range(n):
    board.append(input())

# 체스판 8x8 시작 위치
# 8x8이므로 시작 좌표 => 최소 n-8, m-8
for i in range(n-7):
    for j in range(m-7):
        # 맨 왼쪽위가 흑일 경우
        black_start = 0
        # 맨 왼쪽위가 백일 경우
        white_start = 0

        # 8x8 체스판 탐색
        for a in range(i, i+8):
            for b in range(j, j+8):
                # x, y 좌표의 합 짝수와 홀수는 변을 공유(붙어있음) => 다른 색이어야 함
                # 짝수끼리, 홀수끼리 같은 색
                # x, y 좌표의 합이 짝수
                if (a+b) % 2 == 0:
                    # black이 아니라 white일 때
                    if board[a][b] != 'B':
                        # black 칠하기
                        black_start += 1
                    # white가 아니라 black일 때
                    if board[a][b] != 'W':
                        # white 칠하기
                        white_start += 1

                # x, y 좌표의 합이 홀수
                else:
                    if board[a][b] != 'W':
                        black_start += 1
                    if board[a][b] != 'B':
                        white_start += 1

        # 새로 칠한 칸 수를 리스트에 삽입
        result.append(black_start)
        result.append(white_start)

print(min(result))