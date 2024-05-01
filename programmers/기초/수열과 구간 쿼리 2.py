# 내 풀이
# def solution(arr, queries):
#     answer = []
#     for i in queries:
#         lis = []
#         for idx in range(i[0], i[1]+1):
#             if arr[idx] > i[2]:
#                 lis.append(arr[idx])
#         answer.append(-1 if len(lis) == 0 else min(lis))
#     return answer

# 다른 풀이
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        l = [i for i in arr[s:e+1] if i > k]
        answer.append(-1 if len(l) == 0 else min(l))
    return answer

# for s, e, k in queries
# queries의 각 요소가 길이가 3인 1차원 배열일 때 바로 분해가능

print(solution([0, 1, 2, 4, 3],[[0, 4, 2],[0, 3, 2],[0, 2, 2]]))