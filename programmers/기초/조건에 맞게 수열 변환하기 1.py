def solution(arr):
    for idx, val in enumerate(arr):
        if val >= 50 and val % 2 == 0:
            arr[idx] = val // 2
        elif val < 50 and val % 2 == 1:
            arr[idx] = val * 2
    return arr


print(solution([1, 2, 3, 100, 99, 98]))
