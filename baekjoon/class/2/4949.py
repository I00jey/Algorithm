# 균형잡힌 세상

from collections import deque

while True:
    # 문자열 입력받기
    string = input()
    # 입력 종료 조건
    if string == '.':
        break

    # 괄호를 저장할 큐
    goal_ho = deque()

    for i in string:
        if i == '(':
            goal_ho.append('(')
        elif i == '[':
            goal_ho.append('[')
        # 닫는 대괄호일 경우
        elif i == ']':
            # 저장된 괄호가 없으면
            if len(goal_ho) == 0:
                # 'no' 문자열 넣기
                # 결과에서 균형여부를 구분하기 위해
                goal_ho.append('no')
                break
            # 큐 마지막에 여는 대괄호가 있을 경우
            if goal_ho[-1] == '[':
                # 여는 대괄호 제거
                goal_ho.pop()
            else:
                break
        elif i == ')':
            if len(goal_ho) == 0:
                goal_ho.append('no')
                break
            if goal_ho[-1] == '(':
                goal_ho.pop()
            else:
                break

    # 괄호 큐의 길이로 균형여부 확인
    if len(goal_ho) == 0:
        print('yes')
    else:
        print('no')
