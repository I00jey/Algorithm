def solution(numbers, k):
    answer = numbers[(2*(k-1)) % len(numbers)]
    # 매개변수가 [1, 2, 3, 4], 2 일때,
    # 공을 받는 2번째 사람은 3번이고 인덱스는 2
    # k번째로 공을 던지는 사람보다는 공을 받는 k번째 사람이라고 생각해야 함
    # 공을 안 던졌을때는 인덱스 번호가 0이여야 하니까 k-1
    # 1칸씩 넘어가며 던지니까 곱하기 2
    # 인덱스가 반복되면서 공이 넘어가니까 % 나머지 연산
    return answer


print(solution([1, 2, 3, 4], 2))
print(solution([1, 2, 3, 4, 5, 6], 5))
print(solution([1, 2, 3], 3))