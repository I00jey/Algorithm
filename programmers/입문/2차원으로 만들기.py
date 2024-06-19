def solution(num_list, n):
    answer = [num_list[i:i+n] for i in range(0, len(num_list), n)]
    return answer
# num_list 인덱스 번호를 주어진 수 n만큼 뛰어넘으며,
# 전체 리스트 안에 n만큼 쪼갠 부분 리스트 삽입


# 다른 풀이
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer