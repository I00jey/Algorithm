def solution(my_string):
    answer = [my_string[i::] for i in range(len(my_string))]
    answer.sort()
    return answer

# 오답 정리
# answer = [my_string[i::] for i in range(len(my_string))].sort()
# 위 코드와 같이 값 대입과 동시에 sort()를 할 경우 None이 반환됨
# => sort() 메소드는 리스트를 제자리에서 정렬하고 None을 반환

# 다른 풀이
# return sorted(answer)
# sorted() 메소드는 정렬된 새로운 리스트를 반환

print(solution("banana"))
print(solution("programmers"))