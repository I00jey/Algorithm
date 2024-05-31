def solution(n, slicer, num_list):
    a, b, c = slicer
    if n == 1:
        answer = num_list[:b+1]
    elif n == 2:
        answer = num_list[a:]
    elif n == 3:
        answer = num_list[a:b+1]
    else:
        answer = num_list[a:b+1:c]
    return answer


print(solution(3, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(solution(4, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]))