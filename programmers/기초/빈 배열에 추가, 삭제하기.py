def solution(arr, flag):
    answer = []
    for idx, boo in enumerate(flag):
        if boo == True:
            for i in range(2 * arr[idx]):
                answer.append(arr[idx])
        else:
            for i in range(arr[idx]):
                if answer:
                    answer.pop()
    return answer

# + 연산자를 사용해서 배열에 추가
# for문을 한번 줄일 수 있음
def solution(arr, flag):
    answer = []
    for idx, boo in enumerate(flag):
        if boo == True:
            answer += [arr[idx]] * 2 * arr[idx]
        else:
            for i in range(arr[idx]):
                answer.pop()
    return answer


print(solution([3, 2, 4, 1, 3], [True, False, True, False, False]))