def solution(n):
    answer = 0
    for i in range(n+1):
        if n%2==0:
            if i%2==0:
                answer += pow(i,2)
        else:
            if i%2==1:
                answer += i
    return answer

    # 다른 풀이
    # if n%2:
    #   return sum(range(1, n+1, 2))
    # return sum([i*i for i in range(2, n+1, 2)])

    # range(start, stop, step)
    # 일정 범위의 연속된 정수를 생성하는 데 사용 (주로 for문과 함께 사용)
    # start부터 stop-1까지 step 간격으로 숫자 생성

    # sum(시퀀스 자료형)
    # 여러 숫자들이 포핟된 시퀀스 자료형을 입력받아 그 합계를 반환하는 함수

print(solution(7))
print(solution(10))