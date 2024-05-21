def solution(my_string, queries):
    # 문자열을 리스트로 변환
    # 문자열은 불변이기 때문에 리스트로 변환하여 작업
    answer = list(my_string)
    for query in queries:
        # 슬라이싱과 역순화를 이용해서 부분 문자열 뒤집기
        answer[query[0]:query[1]+1] = answer[query[0]:query[1]+1][::-1]

    # 리스트를 다시 문자열로 변환 (join 사용)
    return ''.join(answer)

# 슬라이싱 slicing
# 범위 추출
# [start:end:step] start 부터 end-1 인덱스 번호 까지 step 칸씩 넘겨 추출
# [:] 전체 추출
# [::-1] 역순 추출

# (TIP) [::-1]을 활용하여 역순 추출을 할 때에는 start가 end보다 커야한다

print(solution("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]]))