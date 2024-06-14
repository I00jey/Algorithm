# 내 풀이
def solution(picture, k):
    answer = []
    for i in picture:
        for j in range(k):
            answer.append(''.join([k*char for char in i]))
    return answer


# 다른 풀이
def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        for _ in range(k):
            answer.append(picture[i].replace('.', '.' * k).replace('x', 'x' * k))
    return answer