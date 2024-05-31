def solution(arr, query):
    for idx, num in enumerate(query):
        if idx % 2 == 0:
            arr = arr[:num+1]
        else:
            arr = arr[num:]
    return arr


print(solution([0, 1, 2, 3, 4, 5], [4, 1, 2]))