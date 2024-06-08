def solution(num_list):
    num_list.sort()
    return num_list[:5]

# 다른 풀이
# return sorted(리스트)[:5]

# .sort() 와 sorted() 의 차이
# sort()
# 리스트 직접 변경, 원본 존재 X
# 반환값 None

# sorted()
# 원본 리스트 변경 X, 원본 존재 O
# 정렬된 새로운 리스트를 반환

# 그러므로 return 뒤에 .sort()를 하면 None이 반환됨