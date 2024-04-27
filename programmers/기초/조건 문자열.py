def solution(ineq, eq, n, m):
    if eq == "!":
        answer = int(eval(str(n) + ineq + str(m)))
    else:
        answer = int(eval(str(n) + ineq + eq + str(m)))
    return answer

    # 다른 풀이
    # if문 사용없이 replace() 함수 사용
    # return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))

    # eval(문자열)
    # : 문자열을 파이썬 코드로 실행

print(solution("<", "=", 20, 50))
print(solution(">", "!", 41, 78))