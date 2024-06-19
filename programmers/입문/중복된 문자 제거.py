def solution(my_string):
    my_string = list(my_string)
    answer = [value for idx, value in enumerate(my_string) if value not in my_string[:idx]]
    return ''.join(answer)


# 다른 풀이
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))

# dict.fromkeys() 메소드를 활용하면, 문자열의 순서대로 딕셔너리 키를 설정 가능
# ''.join()을 통해 딕셔너리 키들을 결합하여 고유한 문자의 문자열 생성