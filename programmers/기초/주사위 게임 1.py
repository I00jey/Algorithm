def solution(a, b):
    answer = 0
    if a%2 and b%2:
        answer = a**2 + b**2
    elif a%2 or b%2:
        answer = 2*(a+b)
    else:
        answer = abs(a-b)
    return answer


# abs 메소드
# abs(number)
# : 주어진 숫자의 절댓값을 반환하는 내장 함수