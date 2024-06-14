def solution(n):
    answer = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                answer[i][j] = 1
            else:
                answer[i][j] = 0
    return answer

# 2차원 배열 초기화
# 배열 초기화를 안하면 list index out of range 에러 발생
# my_list = [[0]*cols for _ in range(rows)]
# my_list = [[i * j for j in range(cols)] for i in range(rows)]


# 다른 풀이
def solution(n):
    answer=[[0]*n for i in range(n)]
    for i in range(n): answer[i][i]=1
    return answer
# 값 1일 넣을 때 이중 for문을 사용하지 않아도 됨