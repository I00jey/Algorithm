def solution(i, j, k):
    answer = 0
    for x in range(i, j+1):
        if str(k) in str(x):
            answer += str(x).count(str(k))
    return answer


# 다른 풀이
def solution(i, j, k):
    answer = sum([str(i).count(str(k)) for i in range(i, j+1)])
    return answer


print(solution(1, 13, 1))
