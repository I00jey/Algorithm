def solution(numlist, n):
    answer = []
    dic = {}
    for i in numlist:
        # 요소와 n과의 거리(절댓값)을 키로 지정
        key = abs(i - n)
        # 만약 이미 딕셔너리에 해당 절댓값이 있다면
        if key in dic:
            # 해당 요소를 리스트에 추가
            dic[key].append(i)
        else:
            # 키-[값] 지정
            dic[key] = [i]

    # 딕셔너리를 키값을 기준으로 정렬시킴
    for key in sorted(dic.keys()):
        values = dic[key]
        # 값(리스트)의 길이가 1일 때
        # => n과의 거리가 유일한 값일 때
        if len(values) == 1:
            # 그대로 리스트에 합치기
            answer.extend(values)
        else:
            # n과의 거리 값이 겹칠 때
            # 내림차순으로 리스트에 합치기
            answer.extend(sorted(values, reverse=True))
    return answer


# 다른 풀이
def solution(numlist, n):
    answer = sorted(numlist, key=lambda x: (abs(x-n), n-x))
    # numlist를 정렬
    # 정렬 기준(key)은 (n과의 차이, n-x)
    # n과의 차이가 같다면 n-x로 정렬
    # n-x는 x(요소)가 클수록 더 앞에 정렬됨
    return answer


# 테스트 케이스
print(solution([1, 2, 3, 4, 5, 6], 4))
print(solution([10000,20,36,47,40,6,10,7000], 30))



# append(element)
# : 리스트 끝에 단일 요소 추가
# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)  # [1, 2, 3, 4]


# extend(iterable)
# : 리스트 끝에 또 다른 리스트의 모든 요소 추가
# my_list = [1, 2, 3]
# my_list.extend([4, 5, 6])
# print(my_list)  # [1, 2, 3, 4, 5, 6]

# * 연산자
# 리스트 언패킹(리스트의 요소를 풀어헤쳐서 개별 요소로 사용하는 것)
# my_list = [1, 2, 3]
# print(*my_list)  # 1 2 3