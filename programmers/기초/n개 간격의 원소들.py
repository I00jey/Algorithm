def solution(num_list, n):
    return num_list[::n]


print(solution([4, 2, 6, 1, 7, 6], 2))
print(solution([4, 2, 6, 1, 7, 6], 4))