def solution(my_string, k):
    answer = ''.join([my_string for _ in range(k)])
    return answer
    # 다른 풀이
    # return my_string*k

print(solution('string',3))