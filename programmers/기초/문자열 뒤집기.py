# def solution(my_string, s, e):
#     return my_string[:s] + my_string[e:s-1 if s > 0 else None:-1] + my_string[e+1:]

# s가 0일 경우 테스트 케이스 실패
# if 문을 통해 예외 처리

# 다른 풀이 (if문 X)
def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]

print(solution("Progra21Sremm3",6, 12))
print(solution("Stanley1yelnatS",4, 10))