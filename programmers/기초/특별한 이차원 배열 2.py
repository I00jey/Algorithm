# 내 풀이
def solution(arr):
    answer = 1
    size = len(arr)
    for i in range(size):
        for j in range(size):
            if arr[i][j] != arr[j][i]:
                answer = 0
    return answer


# 다른 풀이
def solution(arr):
    return int(arr == list(map(list, zip(*arr))))
# zip(*arr)
# arr의 전치 행렬을 생성 (행과 열이 바뀜)
# map(list, zip(*arr))
# 각 튜플을 리스트로 전환
# list(map(...))
# 최종적으로 전치된 2차원 배열을 반환

print(solution([[5, 192, 33], [192, 72, 95], [33, 95, 999]]))
print(solution([[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]]))

# zip()
# 여러 iterable를 인자로 받아 각 iterable의 요소를 묶어 튜플을 생성하는 이터레이터 반환
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [7, 8, 9]
# zipped = zip(a, b, c)
# print(list(zipped))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# * 연산자 (시퀀스 언패킹 연산자)
# 시퀀스의 요소를 개별 인자로 풀어줌
# numbers = [1, 2, 3]
# print(*numbers)  # 1 2 3

