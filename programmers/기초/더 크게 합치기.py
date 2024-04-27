def solution(a, b):
    # 숫자를 붙이기 쉽게 문자형으로 변환
    answer_a = str(a)+str(b)
    answer_b = str(b)+str(a)
    # if문으로 크기 비교 후 반환 answer은 문자형이므로 int 형변환 필요
    return int(answer_a if answer_a >= answer_b else answer_b)

    # 다른 풀이
    # return int(max(f"{a}{b}", f"{b}{a}"))
    # max(a, b)
    # a와 b 중 최댓값 반환

print(solution(9, 91))
print(solution(89, 8))