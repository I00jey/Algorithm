# 내 풀이
def solution(common):
    answer = 0
    if common[1]-common[0] == common[2]-common[1]:
        key = common[1]-common[0]
        answer = common[-1] + key
    else:
        key = common[1]/common[0]
        answer = common[-1]*key
    return answer


# 다른 풀이
def solution(common):
    answer = 0
    a, b, c = common[:3]
    if (b-a) == (c-b):
        return common[-1]+(b-a)
    else:
        return common[-1] * (b//a)