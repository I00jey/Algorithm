def solution(arr):
    answer = []
    for i in arr:
        for j in range(i):
            answer.append(i)
    return answer


print(solution([5, 1, 4]))
print(solution([6, 6]))
print(solution([1]))