from collections import deque
# 나의 풀이
# def solution(s):
#     answer = True
#     que = deque(s)
#     stack = []
#     while que:
#         if que[0] == ')' and len(stack) == 0:
#             answer = False
#             break
#         elif que[0] == '(':
#             stack.append(que.popleft())
#         elif que[0] == ')' and stack[-1] == '(':
#             stack.pop()
#             que.popleft()
#
#     if stack:
#         answer = False
#     return answer


# 코드 최적화
def solution(s):
    stack = []
    for char in s:
        # 열린 괄호이면 스택에 추가
        if char == '(':
            stack.append(char)
        # 닫힌 괄호이면 스택 확인
        elif char == ')':
            # 스택에 비었다면 False 반환
            if not stack:
                return False
            # 스택이 비어있진 않다면 -> '('이 있다면 제거
            stack.pop()
    # 스택이 비어있다면 True
    # 스택이 남아있다면 False
    return not stack


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))

