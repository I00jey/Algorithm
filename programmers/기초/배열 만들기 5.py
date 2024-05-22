def solution(intStrs, k, s, l):
    answer = []
    for intStr in intStrs:
        if int(intStr[s:s+l])>k:
            answer.append(int(intStr[s:s+l]))
    return answer
    # 다른 풀이
    # return [int(intStr[s:s+l]) for intStr in intStrs if int(intStr[s:s+l])>k]
    # [] 리스트 안에 for문 + if문이 있으면, 반복문 내부 if 조건에 해당하는 경우에만 리스트에 값 저장

print(solution(["0123456789","9876543210","9999999999999"],50000,5,5))