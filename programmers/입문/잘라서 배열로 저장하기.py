# 내 풀이
def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
    return answer

# 리스트 컴프리헨션
#  return [my_str[i: i + n] for i in range(0, len(my_str), n)]

