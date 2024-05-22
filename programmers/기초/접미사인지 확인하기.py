def solution(my_string, is_suffix):
    suffix = [my_string[i::] for i in range(len(my_string))]
    return 1 if is_suffix in suffix else 0
    # 다른 풀이
    # return int(my_string[-len(is_suffix):] == is_suffix)
    # my_string 문자열 뒤에서 is_suffix 글자수 만큼의 끊은 글자가 is_suffix와 같다면 True(1) 아니면 False(0)

    # 또 다른 풀이
    # return int(my_string.endswith(is_suffix))
    # str.endswith(suffix[, start[, end]])
    # 특정 문자열이 주어진 접미사로 끝나는지를 확인


print(solution("banana","ana"))
print(solution("banana","nan"))
print(solution("banana","wxyz"))