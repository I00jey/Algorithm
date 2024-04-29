def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if mode == 0:
            if code[i] == '1':
                print("모드변경 1으로")
                mode = 1
            elif code[i] != 1 and i%2 == 0:
                answer += code[i]
        elif mode == 1:
            if code[i] == '1':
                print("모드변경 0으로")
                mode = 0
            elif code[i] != 1 and i%2 == 1:
                answer += code[i]
    return 'EMPTY' if answer == '' else answer

    # 다른 풀이
    # return "".join(code.split("1"))[::2] or "EMPTY"

solution("abc1abc1abc")
