def solution(arr, queries):
    for i in queries:
        temp = arr[i[0]]
        arr[i[0]] = arr[i[1]]
        arr[i[1]] = temp
    return arr

    # 다른 풀이
    # for a, b in queries:
    #     arr[a], arr[b] = arr[b], arr[a]
    # return arr

    # arr[a], arr[b] = arr[b], arr[a]
    # 튜플 언패킹 기능
    # 파이썬에서 변수 값을 교환하는 간단하면서 효율적인 방법

    # for a, b in queries
    # 병렬 할당
    # queries의 각 원소는 [a, b] 형태이므로, for문으로 반복하면
    # a, b에 각각의 원소가 할당됨

print(solution([0, 1, 2, 3, 4],[[0, 3],[1, 2],[1, 4]]))