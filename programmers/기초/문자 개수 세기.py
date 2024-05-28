def solution(my_string):
    answer = [0] * 52
    for word in my_string:
        if word.isupper():
            answer[ord(word)-65] += 1
        else:
            answer[ord(word)-71] += 1
    return answer

print(solution("Programmers"))

print(ord('A'))
print(ord('a'))


# 아스키 코드 ASCII code
# 각 문자에 대해 고유한 숫자를 지정하는 표준

# ord() : 문자를 입력받아 그에 대응하는 아스키 코드 값 변환
# ex) 'A' -> 65 / 'a' -> 97

# chr() : 아스키 코드 값을 입력받아 그에 대응하는 문자를 반환