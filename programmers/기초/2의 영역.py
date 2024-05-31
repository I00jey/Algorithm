# 내 풀이
def solution(arr):
    if arr.count(2) < 1:
        return [-1]
    arr2 = []
    for idx, num in enumerate(arr):
        if num == 2:
            arr2.append(idx)
    if len(arr2) == 1:
        return arr[arr2[0]:arr2[0]+1]
    else:
        return arr[arr2[0]:arr2[-1]+1]


# 다른 풀이
def solution(arr):
    if 2 not in arr:
        # 배열에 값 2가 없으면 [-1] 반환
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]
    # 배열.index(2)
    # 배열 처음부터 값 2를 찾아서 해당 인덱스 반환
    # len(arr) - arr[::-1].index(2)
    # 배열을 [::-1]을 통해 뒤집은 다음 앞에서부터 2 인덱스 찾기
    # 배열의 길이에서 해당 인덱스를 빼면 원본 배열의 마지막 2 다음 인덱스 번호가 나옴
    # 그대로 슬라이싱 넣으면 마지막 2까지 포함된 배열 반환



print(solution([1, 2, 1, 4, 5, 2, 9]))
print(solution([1, 2, 1]))
print(solution([1, 1, 1]))
print(solution([1, 2, 1, 2, 1, 10, 2, 1]))