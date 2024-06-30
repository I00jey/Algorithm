# 내 풀이
def solution(num, total):
    # start부터 연속된 num개의 수의 합 = total
    # total = (start)*num + (1부터 num-1 까지의 합)
    plus = sum([i for i in range(num)])
    # plus = 1부터 num-1 까지의 합
    start = (total-plus)//num
    # 연속된 세 개의 정수 중 최솟값 구하기
    answer = [start + i for i in range(num)]
    # 최솟값부터 1씩 더한 배열 반환
    return answer


# 다른 풀이