def solution(arr):
    count = 0
    nochange = 0
    while True:
        for idx, val in enumerate(arr):
            if val >= 50 and val % 2 == 0:
                arr[idx] = val // 2
            elif val < 50 and val % 2 == 1:
                arr[idx] = val * 2 + 1
            else:
                nochange += 1
        if nochange == len(arr):
            break
        count += 1
        nochange = 0
    return count


print(solution([1, 2, 3, 100, 99, 98]))