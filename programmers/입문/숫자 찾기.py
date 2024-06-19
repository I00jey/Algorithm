def solution(num, k):
    answer = -1
    for i, v in enumerate(list(str(num))):
        if v == str(k):
            answer = i + 1
            return answer
    return answer


def solution(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1



# find 함수
# 문자열 내에서 부분 문자열을 찾아서 시작 인덱스 반환
# str.find(sub[, start[, end]])
# 부분 문자열이 존재하지 않으면 -1 반환

# index 함수
# 문자열 내에서 문자열을 찾아서 시작 인덱스 반환
# str.index(sub[, start[, end]])
# 부분 문자열이 존재하지 않으면 ValueError 예외 발생
