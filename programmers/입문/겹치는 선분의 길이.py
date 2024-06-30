# 내 풀이 (정확성 : 70.0)
# 문제점 => 선분 3개가 겹치는 부분이 있는 경우, 같은 부분을 2번 더해 오류 발생
# def solution(lines):
#     answer = 0
#     lines.sort()
#     combs = [[0, 1], [0, 2], [1, 2]]
#     for comb in combs:
#         # 두 선분이 안 겹칠 때
#         if lines[comb[0]][1] <= lines[comb[1]][0]:
#             continue
#         else:
#             answer += lines[comb[0]][1] - lines[comb[1]][0]
#     return answer


# 다른 풀이
def solution(lines):
    # 모든 점을 저장할 리스트를 생성
    points = []

    # 각 선분의 시작과 끝 점을 points 리스트에 추가
    for line in lines:
        start, end = line
        points.append((start, 1))  # 선분의 시작점
        points.append((end, -1))  # 선분의 끝점

    # points 리스트를 정렬
    points.sort()

    overlap_length = 0
    current_overlap = 0
    prev_point = points[0][0]
    print(points)

    # 각 점을 순회하며 겹치는 부분을 계산
    for point, value in points:
        if current_overlap > 1:  # 두 개 이상의 선분이 겹치는 경우
            overlap_length += point - prev_point

        current_overlap += value
        prev_point = point

    return overlap_length


# 다른 풀이
def solution2(lines):
    # 주어진 3개의 선분을 포함한 범위(집합)을 리스트에 저장
    sets = [set(range(min(l), max(l))) for l in lines]
    # 각 선분이 겹치는 범위들(교집합)의 합집합을 반환
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])


print(solution([[0, 5], [3, 9], [1, 10]]))