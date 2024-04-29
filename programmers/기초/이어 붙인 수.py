def solution(num_list):
    even = ''
    odd = ''
    for value in num_list:
        if value%2==0:
            even += str(value)
        else:
            odd += str(value)
    return int(even) + int(odd)

    # 다른 풀이
    # return int(''.join([str(x) for x in num_list if x % 2])) + int(''.join([str(x) for x in num_list if not x % 2]))

print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))