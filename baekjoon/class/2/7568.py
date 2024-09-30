# 덩치

# 내 풀이 (실패)

# 입력받을 사람 수
# n = int(input())
#
# dung_chi = []
# # 몸무게, 키 입력
# for i in range(n):
#     weight, height = map(int, input().split())
#     dung_chi.append([weight, height])
#
# sort_dung_chi = sorted(dung_chi, reverse=True)
# # print(dung_chi)
# # print(sort_dung_chi)
#
# sort_score = [0] * len(dung_chi)
# rank = 1
# for i in range(1, len(dung_chi)):
#     if sort_dung_chi[i-1][1] > sort_dung_chi[i][1]:
#         # print(sort_dung_chi[i-1][1], '>', sort_dung_chi[i][1])
#         if sort_score[i-1] == 0:
#             sort_score[i-1] = i
#         sort_score[i] = i+1
#         rank += 1
#     else:
#         # print(sort_dung_chi[i - 1][1], '<=', sort_dung_chi[i][1])
#         sort_score[i-1] = rank
#         sort_score[i] = rank
#
#
# for i in range(len(dung_chi)):
#     dung_chi[i] = sort_score[sort_dung_chi.index(dung_chi[i])]
#
# for i in dung_chi:
#     print(i, end=' ')


# --------------------------------------------------------------------
# 다른 풀이
# 완전 탐색
# 자기보다 덩치가 큰 사람이 몇명인지 세서 등수 구하기

# 사람 수
num_student = int(input())
student_list = []
for _ in range(num_student):
    # 몸무게, 키 입력
    weight, height = map(int, input().split())
    student_list.append((weight, height))


for i in student_list:
    # 순위 기본값 1
    rank = 1
    for j in student_list:
        # 입력받은 A의 덩치를 다른 모든 사람의 덩치와 비교
        if i[0] < j[0] and i[1] < j[1]:
            # A보다 덩치가 큰 사람 수대로 등수 내리기
            rank += 1
    print(rank, end=' ')

