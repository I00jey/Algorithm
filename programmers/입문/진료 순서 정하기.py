# 내 풀이
def solution(emergency):
    answer = []
    arr = sorted(emergency)[::-1]
    for value in emergency:
        answer.append(arr.index(value)+1)
    return answer


# 다른 풀이
def solution(emergency):
    e = sorted(emergency, reverse=True)
    return [e.index(i)+1 for i in emergency]



print(solution([3, 76, 24]))
print(solution([1, 2, 3, 4, 5, 6, 7]))
print(solution([30, 10, 23, 6, 100]))


# sorted()
# : iterable 객체를 정렬하여 반환
# 원본을 변경하지 않고, 새로운 리스트 반환

# sorted(iterable, *, key=None, reverse=False)
# iterable : 정렬할 대상이 되는 반복 가능한 객체
# key : 정렬 기준이 되는 함수, 기본 값은 None / 예시) key=len
# reverse : 정렬 순서를 역순으로 할지 여부를 나타내는 부울 값, 기본 값 False / True면 내림차순


