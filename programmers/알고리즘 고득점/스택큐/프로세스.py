from collections import deque


def solution(priorities, location):
    answer = 0
    processes = [chr(ord('A')+i) for i in range(len(priorities))]
    target = processes[location]
    arr = list(zip(priorities, processes))
    que = deque(arr)
    output = []
    while que:
        current_process = que.popleft()
        if not que or current_process[0] >= max(que)[0]:
            output.append(current_process[1])
        else:
            que.append(current_process)
    answer = output.index(target)+1
    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
