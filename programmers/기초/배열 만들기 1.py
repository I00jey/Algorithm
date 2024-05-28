def solution(n, k):
    answer = [k * i for i in range(1, n // k +1)]
    return answer


print(solution(10, 3))
print(solution(15, 5))