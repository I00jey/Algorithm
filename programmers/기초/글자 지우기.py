def solution(my_string, indices):
    my_string = list(my_string)
    for i in indices:
        my_string[i] = ''
        # del 사용 가능
        # del my_string[i]
    return ''.join(my_string)


print(solution("apporoograpemmemprs", [1, 16, 6, 15, 0, 10, 11, 3]	))

# 문자열은 불변 객체이기 때문에 직접적으로 수정불가
# 새로운 문자열을 만들어서 할당해야 함