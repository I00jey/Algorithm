# 내 풀이
def solution(str_list):
    if 'l' in str_list and 'r' in str_list:
        if str_list.index('l') < str_list.index('r'):
            answer = str_list[:str_list.index('l')]
        else:
            answer = str_list[str_list.index('r')+1:]
    elif 'l' in str_list and 'r' not in str_list:
        answer = str_list[:str_list.index('l')]
    elif 'l' not in str_list and 'r' in str_list:
        answer =  str_list[str_list.index('r')+1:]
    else:
        return []
    return answer

# 다른 풀이
def solution(str_list):
    for idx, str in enumerate(str_list):
        if str == 'l':
            return str_list[:idx]
        elif str == 'r':
            return str_list[idx+1:]
    return []

print(solution(["u", "u", "l", "r"]))
print(solution(["u", "u", "l"]))
print(solution(["l"]))