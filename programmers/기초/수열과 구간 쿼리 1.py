def solution(arr, queries):
    for s, e in queries:
        for i in range(s, e+1):
            arr[i] += 1

        # 다른 풀이
        # arr = [a+1 if s <= i <= e else a for i, a in enumerate(arr)]
    return arr


print(solution([0, 1, 2, 3, 4], [[0, 1],[1, 2],[2, 3]]))