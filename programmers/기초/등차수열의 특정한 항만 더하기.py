def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i] == True:
            answer += a + d*i
    return answer
    # 다른 풀이
    # return sum(a + i * d for i, f in enumerate(included) if f)

    # enumerate(순서가 있는 자료형)
    # : 인덱스와 값을 포함하여 리턴 (튜플형태)
    # 인덱스와 값을 동시에 접근하면서 루프를 돌리고 싶을 때 사용

print(solution(3,4,[True, False, False, True, True]))
print(solution(7,1,[False, False, False, True, False, False, False]))