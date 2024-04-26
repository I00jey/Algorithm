def solution(my_string, overwrite_string, s):
    # 원본 문자열 (주어진 인덱스 전까지) + 교체할 문자열 + 원본 문자열 (교차 문자열이 끝나는 시점부터 끝까지)
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer

print(solution("He11oWor1d","lloWorl", 2))
# HelloWorld
print(solution("Program29b8UYP","merS123", 7))
# ProgrammerS123