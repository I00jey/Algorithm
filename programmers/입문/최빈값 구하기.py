def solution(array):
    answer = 0
    dic = dict.fromkeys(array, 0)
    for i in array:
        dic[i] += 1
    print(dic)
    max_value = max(dic.values())
    arr = [key for key, value in dic.items() if value == max_value]
    if len(arr) >= 2:
        answer = -1
    else:
        answer = arr[0]
    return answer


print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))

