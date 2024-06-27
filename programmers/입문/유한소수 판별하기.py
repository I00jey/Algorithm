# 내 풀이 (테스트 케이스 통과, 정확성 83.3)
def solution(a, b):
    if a%b==0:
        return 1
    max_yak_su = 1
    arr_a = sorted([i for i in range(1, a+1) if a%i == 0], reverse=True)
    arr_b = sorted([i for i in range(1, b+1) if b%i == 0], reverse=True)
    for i in arr_a:
        if i in arr_b:
            max_yak_su = i
            break
    after_b = b // max_yak_su
    print(after_b)
    yaksu_b = [i for i in range(1, after_b + 1) if after_b % i == 0]
    sosu_b = [i for i in yaksu_b if len([j for j in range(1, i+1) if i % j == 0]) == 2]
    print(sosu_b)
    return 2 if not (2 in sosu_b or 5 in sosu_b) else 1


print(solution(4, 125))

# 다른 풀이
# gcd Greatest Common Divisor 최대공약수
# math 라이브러리에 내장되어 있는 함수
from math import gcd
def solution(a, b):
    # 분모와 분자의 최대공약수로 분모 나누기
    b //= gcd(a, b)
    # 2로 나눠지지 않을 때까지 나누기
    while b % 2 == 0:
        b //= 2
    # 5로 나눠지지 않을 때까지 나누기
    while b % 5 == 0:
        b //= 5
    # 최종 b가 1이면 1 반환 아니면 2 반환
    # b == 1  => 기약분수에서 분모의 소인수가 2와 5만 존재함
    return 1 if b == 1 else 2


# 내 풀이에 적용해보기
def solution(a, b):
    if a%b==0:
        return 1
    max_yak_su = 1
    arr_a = sorted([i for i in range(1, a+1) if a%i == 0], reverse=True)
    arr_b = sorted([i for i in range(1, b+1) if b%i == 0], reverse=True)
    for i in arr_a:
        if i in arr_b:
            max_yak_su = i
            break
    b = b // max_yak_su
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    return 1 if b == 1 else 2
