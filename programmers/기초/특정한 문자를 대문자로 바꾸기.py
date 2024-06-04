# def solution(my_string, alp):
#     my_string = list(my_string)
#     for idx, str in enumerate(my_string):
#         if str == alp:
#             my_string[idx] = alp.upper()
#     return ''.join(my_string)


def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())

# replace(old, new, [count])
# 문자열 안에서 특정 문자를 새로운 문자열 변경하는 기능
# (변경할 문자, 새로 바꿀 문자, 변경할 횟수)
# 변경할 횟수를 입력하지 않으면 문자열 전체 변경


print(solution("programmers", "p"))
print(solution("lowercase", "x"))