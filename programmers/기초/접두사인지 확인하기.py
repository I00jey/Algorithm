# def solution(my_string, is_prefix):
#     answer = int(my_string.startswith(is_prefix))
#     return answer

# 다르게 풀어보기
def solution(my_string, is_prefix):
    return 1 if is_prefix == my_string[:len(is_prefix)] else 0


print(solution("banana","ban"))
print(solution("banana", "nan"))
print(solution("banana", "abcd"))
print(solution("banana", "bananan"))