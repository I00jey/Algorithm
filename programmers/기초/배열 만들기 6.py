def solution(arr):
    answer = []
    i = 0
    while i < len(arr):
        if answer:
            if answer[-1] == arr[i]:
                answer.pop()
                i += 1
            else:
                answer.append(arr[i])
                i += 1
        else:
            answer.append(arr[i])
            i += 1
    return answer if answer else [-1]


print(solution([0, 1, 1, 1, 0]))
print(solution([0, 1, 0, 1, 0]))
print(solution([0, 1, 1, 0]))