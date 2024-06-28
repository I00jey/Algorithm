def solution(sides):
    arr = []
    # 주어진 배열의 최댓값 = 삼각형 가장 긴 변 경우
    long = max(sides)
    for i in range(1, long+1):
        if min(sides) + i > long:
            arr.append(i)

    # 주어진 배열에 삼각형 가장 긴 변이 포함이 안된 경우
    # 가장 긴 변이 sides 원소가 아니므로 sides 원소 범위 사용 X
    for i in range(long+1, sum(sides)):
        if long < i < sum(sides):
            arr.append(i)
    return len(arr)


print(solution([1, 2]))
print(solution([3, 6]))
print(solution([11, 7]))
print(solution([1000, 1000]))

# 다른 풀이
def solution(sides):
    return 2 * min(sides) - 1

# 삼각형 3변 a, b, x
# 1. b가 가장 클 때
# b < a + x
# ⭐ b - a < x
# 2. x가 가장 클 때
# ⭐ x < a + b

# 이 두 조건을 합하면
# b - a < x < a + b
# x의 개수는 a+b - (b-a) - 1 = 2a - 1
# 여기서 a는 sides 배열의 최솟값

