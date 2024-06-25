def solution(spell, dic):
    answer = 2
    for i in dic:
        if sorted(spell) == sorted(i):
            # spell의 모든 알파벳 요소를 사용해야 하므로
            # spell과 dic의 문자열을 정렬시켰을 때 동일하면 1 반환
            answer = 1
    return answer


# 다른 풀이
def solution(spell, dic):
    spell = set(spell)
    # spell 리스트를 집합으로 변환
    # 집합은 중복 X 순서 X
    for s in dic:
        if not spell-set(s):
            # spell에서 s를 집합으로 변환한 것을 뺌
            # spell에만 있고 set(s)에는 없는 요소들로 이루어진 집합이 반환
            # not spell-set(s)
            # 결과가 빈 집합이라면 => spell의 모든 요소가 set(s)에 포함되어 있으면
            # 1 반환
            return 1
    return 2