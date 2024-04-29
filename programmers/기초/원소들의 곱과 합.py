def solution(num_list):
    mul = 1
    powsum = 0
    for i in num_list:
        mul *= i
        powsum += i
    return 1 if mul < pow(powsum,2) else 0

print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))