def solution(my_string, index_list):
    answer = ''.join(my_string[i] for i in index_list)
    return answer

print(solution("cvsgiorszzzmrpaqpe",[16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]))
print(solution("zpiaz",[1, 2, 0, 0, 3]))