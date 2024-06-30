def solution(babbling):
    answer = 0
    # 조카가 가능한 발음
    words = ["aya", "ye", "woo", "ma"]
    for babble in babbling:
        original_babble = babble
        for word in words:
            # 단어에 조카가 가능한 발음이 포함되어 있는 경우
            if word in babble:
                # 해당 발음을 " " 공백으로 대체
                # "" 빈 문자열로 대체하는 않는 이유
                # => "wyeoo"의 경우 "ye"를 빈문자열로 대체하면 "w"+"oo"가 합쳐져서 "woo"가 되기 때문에 예외 발생
                babble = babble.replace(word, " ")
                # print(original_babble, word, babble)
            else:
                continue
        if babble.strip() == "":
            # 문자열 앞 뒤에 공백을 제거한 후 빈 문자열이라면
            # (= 해당 단어가 가능한 발음으로만 구성되어 있는 경우)
            answer += 1
    return answer


# 다른 풀이
import re
# 정규 표현식을 사용하기 위해 re 모듈 임포트
def solution(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    # 정규 표현식 컴파일
    # '^' : 문자열의 시작
    # '(aya|ye|woo|ma)' : aya, ye, woo, ma 중 하나
    # '+' : 하나 이상의 앞의 패턴(여기서는 aya, ye, woo, ma 중 하나)이 반복될 수 있음
    # '$' : 문자열의 끝
    # 문자열 전체가 aya, ye, woo, ma 중 하나 이상으로만 구성되어 있는지 검사
    cnt = 0
    for e in babbling:
        # 현재 문자열 'e'가 정규 표현식에 맞는지 검사
        if regex.match(e):
            cnt += 1
    return cnt


print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))