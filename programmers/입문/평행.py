# 내 풀이
def solution(dots):
    answer = 0
    # 4개의 점을 2개씩 잇는 조합을 저장한 배열
    combs = [[[0, 1], [2, 3]], [[0, 2], [1, 3]], [[0, 3], [1, 2]]]
    for comb in combs:
        # 두 선의 기울기를 저장할 배열 선언 및 초기화
        slope = []
        # 선 [점 인덱스, 점 인덱스]
        for line in comb:
            # x 이동값
            dx = dots[line[0]][0]-dots[line[1]][0]
            # y 이동값
            dy = dots[line[0]][1]-dots[line[1]][1]
            # 기울기 = y 이동값 / x 이동값
            slope.append(dy/dx)
        # 기울기 배열에 저장된 기울기 값이 2개이고, 두 값이 같을 경우
        if len(slope) == 2 and slope[0] == slope[1]:
            answer += 1
    return 1 if answer else 0


print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))

