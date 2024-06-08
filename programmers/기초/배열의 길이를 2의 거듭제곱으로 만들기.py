def solution(arr):
    n = 0
    while 2 ** n < len(arr):
        n += 1
    arr.extend([0] * (2 ** n - len(arr)))
    return arr

# 마지막 테스트 케이스만 틀림
# 2번째 줄 n을 0부터 시작해야 함
# 2 ** 0 == 1 이고 arr는 1부터 1000까지의 숫자라고 조건이 있음

print(solution([1, 2, 3, 4, 5, 6]))
print(solution([58, 172, 746, 89]))
print(solution([1]))
