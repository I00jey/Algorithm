def solution(myString):
    answer = ''
    for i in myString:
        if ord(i) < ord('l'):
            answer += 'l'
        else:
            answer += i
    return answer


# 아스키 코드 함수
# ord() 문자 -> 아스키
# chr() 아스키 -> 문자
