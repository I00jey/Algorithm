# 내 풀이
def solution(A, B):
    answer = 0
    for i in range(len(A)):
        if A == B:
            return answer
        A = A[-1] + A[:len(A)-1]
        answer += 1
    return -1


# 다른 풀이
def solution(a, b):
    return (b*2).find(a)
    # 부분 문자열의 인덱스를 찾아 반환
    # 없다면 -1 반환