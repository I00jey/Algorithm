def solution(str_list, ex):
    return ''.join([i for i in str_list if ex not in i])


# 리스트 컴프리헨션
# [expression for item in iterable if condition]
# expression : 리스트의 각 요소가 될 항목
# item : 반복 변수
# iterable : 반복 가능한 객체
# condition : item에 대해 조건을 평가하는 부분