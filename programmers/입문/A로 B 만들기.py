def solution(before, after):
    dic_before = {}
    dic_after = {}
    for i in before:
        if i in dic_before.keys():
            dic_before[i] += 1
        else:
            dic_before[i] = 1

    for i in after:
        if i in dic_after.keys():
            dic_after[i] += 1
        else:
            dic_after[i] = 1
    return 1 if dic_before.items() == dic_after.items() else 0


# 다른 풀이
def solution(before, after):
    before = sorted(before)
    after = sorted(after)
    print(before)   # ['e', 'h', 'l', 'l', 'o']
    print(after)    # ['e', 'h', 'l', 'l', 'o']
    if before == after:
        return 1
    else:
        return 0


# sorted( )
# 문자열은 iterable 이므로 각 알파벳을 개별 요소로 처리
# 문자들을 정렬한 뒤 리스트로 변환


solution("olleh", "hello")
solution("allpe", "apple")