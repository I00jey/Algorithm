def solution(M, N):
    answer = (M-1) + M*(N-1)
    # 먼저 세로를 M-1번 잘라 M조각으로 만들고
    # M조각들을 가로로 N-1번씩 잘라야 함
    return answer

