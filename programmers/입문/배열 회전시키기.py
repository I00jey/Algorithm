# 내 풀이
def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer = numbers[-1::] + numbers[:len(numbers)-1:]
    else:
        answer = numbers[1::1]
        answer.append(numbers[0])
    return answer


# 다른 풀이
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]
# 방향이 right 일 경우
# 배열의 맨 끝 숫자가 앞으로 오고 그 뒤에 나머지 배열이 옴
# 방향이 left 일 경우
# 배열의 맨 앞 숫자가 뒤로 가고 앞에서부터 나머지 배열이 옴


print(solution([1, 2, 3], "right"))
print(solution([4, 455, 6, 4, -1, 45, 6], "left"))
