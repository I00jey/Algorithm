def solution(my_strings, parts):
    answer = ''
    for idx, my_string in enumerate(my_strings):
        answer += my_string[parts[idx][0]:parts[idx][1]+1]
    return answer

print(solution(["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]]))