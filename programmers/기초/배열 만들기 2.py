# 정규식 풀이
# re.match(정규식, 비교할 대상)
# True or False

import re
def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if re.match('^[05]+$', str(i)):
            answer.append(i)
    return [-1] if len(answer)==0 else answer

# 다른 풀이
# set(iterable)
# 반복 가능한 객체를 입력으로 받아 중복된 요소를 제거하고 유일한 값들을 포함하는 새로운 집합 생성

# def solution(l, r):
#     answer = []
#     for num in range(l, r + 1):
#         if not set(str(num)) - set(['0', '5']):
#             answer.append(num)
#     return answer if answer else [-1]


print(solution(5,555))
print(solution(10,20))