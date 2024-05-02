def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk.pop()
    return stk

# 다른 풀이
# def solution(arr):
#     stk = []
#     for i in range(len(arr)):
#         while stk and stk[-1] >= arr[i]:
#             stk.pop()
#         stk.append(arr[i])
#     return stk
# 문제 속 조건에서 i는 1씩 증가하므로 for i in range(len(arr))을 통해서 반복문을 돌릴 수 있음

print(solution([1, 4, 2, 5, 3]))