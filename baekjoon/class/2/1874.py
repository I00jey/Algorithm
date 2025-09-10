# # 스택큐 수열
#
# # 내 풀이 (시간 초과)
# import sys
# input = sys.stdin.readline
#
# # n 입력 받기
# n = int(input())
#
# # 수열
# series = []
# # 수열 입력받기
# for _ in range(n):
#     series.append(int(input()))
#
# # print("수열 => ", series)
#
# # 스택큐 리스트
# stack = []
# # push & pop 연산 리스트
# push_pop = []
# # push 수 리스트
# push = []
#
# # 스택큐 초기화
# for i in range(1, series[0]+1):
#     stack.append(i)
#     push_pop.append("+")
#     push.append(i)
#
# # print("스택큐 초기화 => ", stack)
#
# # push & pop 연산 순서 구하기
# for idx, num in enumerate(series):
#     # print(str(num) + "차례")
#     if stack:
#         if stack[-1] == num:
#             stack.pop()
#             push_pop.append("-")
#             # print("pop 연산 후 stack => ", stack)
#         else:
#             for i in range(max(push) + 1, num + 1):
#                 stack.append(i)
#                 push.append(i)
#                 push_pop.append("+")
#                 # print("push 연산 후 stack => ", stack)
#
#             if stack[-1] == num:
#                 stack.pop()
#                 push_pop.append("-")
#                 # print("pop 연산 후 stack => ", stack)
#             else:
#                 push_pop.append("NO")
#     else:
#         for i in range(max(push)+1, num+1):
#             stack.append(i)
#             push.append(i)
#             push_pop.append("+")
#             # print("push 연산 후 stack => ", stack)
#
#         if stack[-1] == num:
#             stack.pop()
#             push_pop.append("-")
#             # print("pop 연산 후 stack => ", stack)
#         else:
#             push_pop.append("NO")
#
#
# if 'NO' in push_pop:
#     print("NO")
# else:
#     for i in push_pop:
#         print(i)
#
#


# ----------------------------------------------

# 다른 풀이
import sys
input = sys.stdin.readline

# n 입력 받기
n = int(input())

# 수열 입력 받기
series = [int(input()) for _ in range(n)]

# 스택큐 리스트와 연산 기록
stack = []
push_pop = []
push = []
max_push = 0  # 현재까지 푸시된 가장 큰 수

# push & pop 연산 순서 구하기
for num in series:
    # 스택에 요소가 있고 마지막 요소가 수열과 일치할 경우, pop
    if stack and stack[-1] == num:
        stack.pop()
        push_pop.append("-")
    elif num > max_push:
        # push 최댓값보다 수열 수가 큰 경우, push ( 최댓값+1 부터 num 까지 )
        for i in range(max_push + 1, num + 1):
            stack.append(i)
            push_pop.append("+")
        # push 최댓값 num을 max_push에 저장
        max_push = num
        stack.pop()
        push_pop.append("-")
    else:
        # num이 이미 스택에 있어야 하는데 없다면 불가능한 수열
        push_pop.append("NO")
        break

if "NO" in push_pop:
    print("NO")
else:
    for i in push_pop:
        print(i)
