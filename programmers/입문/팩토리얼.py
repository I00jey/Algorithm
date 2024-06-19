def solution(n):
    answer = 0
    total = 1
    while total <= n:
        answer += 1
        total *= answer
    return answer-1

# answer 정수 값을 1씩 더하면서 팩토리얼 결과값인 total에 곱함
# total이 주어진 값 n보다 커지면 1을 뺀 값을 리턴



# 다른 풀이
from math import factorial
def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k