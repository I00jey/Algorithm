def solution(score):
    answer = []
    avg = [sum(i)/2 for i in score]
    # 두 과목 점수의 평균 리스트 생성
    sort_avg = sorted(avg, reverse=True)
    # 평균 점수를 내림차순으로 정렬
    for i in avg:
        answer.append(sort_avg.index(i)+1)
        # 빈 배열에 원본 배열의 순서대로 등수 저장
        # 등수 = 인덱스 + 1 (1부터 시작)
        # 평균 점수가 같을 땐
        # => 내림차순 배열에서 index 함수가 지정 평균점수의 첫번째 요소 인덱스를 반환
    return answer


# 다른 풀이
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]