# def solution(rank, attendance):
#     score = []
#     arr = 1
#     # 등수는 1부터 시작하므로 while 조건문을 사용
#     # 3명이 모이면 while문 종료
#     while len(score) < 3:
#         if attendance[rank.index(arr)]:
#             score.append(rank.index(arr))
#             # 해당 등수의 학생이 참여했다면 (True) 배열에 넣기
#         arr += 1
#     return 10000 * score[0] + 100 * score[1] + score[2]


def solution(rank, attendance):
    arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])
    # sorted()는 기본적으로 튜플의 첫번째 요소를 기준으로 정렬 (참석한 학생 중 등수 기준)
    return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]
    # return arr  # [(2, 2), (4, 4), (5, 3), (7, 1)]


print(solution([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False]))