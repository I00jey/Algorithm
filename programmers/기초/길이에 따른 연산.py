# 내 풀이
def solution(num_list):
    answer = 1
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for i in num_list:
            answer *= i
        return answer


# 다른 풀이
from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list)>= 11 else prod(num_list)


print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))
print(solution([2, 3, 4, 5]))