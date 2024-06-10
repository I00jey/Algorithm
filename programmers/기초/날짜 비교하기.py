# 첫번째 풀이
def solution(date1, date2):
    return int(date1 < date2)

# 파이썬에선 시퀀스(배열, 문자열, ...) 비교 가능 O
# 왼쪽에서 오른쪽으로 비교

# 예시) [4, 4, 4] > [4, 3, 5]

# 두번째 풀이
def solution(date1, date2):
    for i in range(len(date1)):
        if date1[i] < date2[i]: return 1
    return 0

print(solution([2021, 12, 28], [2021, 12, 29]))