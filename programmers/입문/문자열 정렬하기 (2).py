def solution(my_string):
    return ''.join(sorted([i.lower() for i in my_string]))


# 다른 풀이
def solution(my_string):
    return ''.join(sorted(my_string.lower()))

# 문자열.lower()
# 문자열을 소문자로 변환하는데 사용되는 문자열 메소드


# 다른 풀이
def solution(my_string):
    answer = []
    for i in my_string:
        if ord('A') <= ord(i) <= ord('Z'):
            answer.append(chr(ord(i)+32))
        else:
            answer.append(i)
    return ''.join(sorted(answer))


print(ord('a'))     # 97
print(ord('z'))     # 122
print(ord('A'))     # 65
print(ord('Z'))     # 90
