def solution(n_str):
    answer = ''
    for i in range(len(n_str)):
        if n_str[i] != '0':
            answer = n_str[i:]
            break
    return answer

# 다른 풀이
def solution(n_str):
    return n_str.lstrip('0')

# lstrip() 함수
# 문자열의 왼쪽에서 특정 문자를 제거
# 기본적으로 공백 제거
# 원본 문자열을 변경하지 않고, 새로운 문자열 반환

print(solution("0010"))
print(solution("854020"))

