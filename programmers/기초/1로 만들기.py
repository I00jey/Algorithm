def solution(num_list):
    count = 0
    for num in num_list:
        while num != 1:
            num = num / 2 if num % 2 == 0 else (num - 1)/2
            count += 1
    return count


print(solution([12, 4, 15, 1, 14]))