# 내 풀이
def solution(balls, share):
    a, x, y = 1, 1, 1
    for i in range(1, balls+1):
        a *= i
    for i in range(1, balls-share+1):
        x *= i
    for i in range(1, share+1):
        y *= i
    return a // (x*y)


# 다른 풀이
import math
def solution(balls, share):
    return math.comb(balls, share)

# math.comb(balls, share)
# balls 전체 공의 수
# share 선택할 공의 수
# balls 개의 공에서 share 개의 공을 선택하는 조합의 수 반환


print(solution(3, 2))
print(solution(5,3))