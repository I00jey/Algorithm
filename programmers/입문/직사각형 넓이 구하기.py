# 내 풀이
def solution(dots):
    answer = 0
    arr_x = [i[0] for i in dots]
    arr_y = [i[1] for i in dots]
    x = max(arr_x)-min(arr_x)
    y = max(arr_y)-min(arr_y)
    return x*y


# 다른 풀이
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])
# dots 배열의 최댓값 (사각형의 오른쪽 상단 꼭짓점의 좌표)
# dots 배열의 최솟값 (사각형의 왼쪽 하단 꼭짓점의 좌표)
# 사각형 각 좌표의 최댓값과 최솟값을 빼면 사각형의 가로, 세로