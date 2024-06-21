def solution(array, n):
    arr = [abs(n-i) for i in array]
    # 리스트의 요소들과 n과 뺄셈의 절댓값을 저장
    num = [array[idx] for idx, num in enumerate(arr) if num == min(arr)]
    # 절댓값 중 최소값을 가지고 있는 arr 요소들의 index를 활용해 n과 제일 가까운 요소(1개 이상)을 저장
    return min(num)


# 다른 풀이
def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    # array를 제자리에서 정렬 (원본 X)
    # 정렬의 기준이 되는 키를 지정
    # abs(x-n) : x과 n의 차이의 절댓값
    # x-n : x과 n의 차이
    # x와 n의 절댓값 차이로 정렬
    # 절댓값 차이가 같은 경우, x과 n의 차이에 따라 정렬
    # (x가 작은 순서대로 정렬됨)
    answer = array[0]
    return answer