def solution(arr, delete_list):
    answer = []
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr


# 배열에서 요소를 삭제하는 방법

# 1. del 키워드
# del 리스트[인덱스]

# 2. remove 메소드
# 리스트.remove(값)

# 3. pop 메소드
# 리스트.pop(인덱스)

# 리스트 컴프리헨션
# arr = [x for x in arr if x != 3]
# 특정 조건에 맞지 않는 요소만 남기는 방법