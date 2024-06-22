# 수정 전 코드
def solution(s):
    answer = 0
    arr = s.split(' ')
    print(arr)
    for idx, value in enumerate(arr):
        if value == 'Z':
            answer -= int(arr[idx-1])
        elif value.isdigit():
            answer += int(value)
    return answer

# "-1 -2 -3 Z" 테스트 케이스에서 오류 발생
# isdigit() : 문자열이 숫자로만 이루어져 있는지 확인하는 메소드
# 음수 기호 - 나 소수점 . 이 포함된 경우 False를 반환



# 수정 후 코드
def solution(s):
    answer = 0
    arr = s.split(' ')
    print(arr)
    for idx, value in enumerate(arr):
        if value == 'Z':
            answer -= int(arr[idx-1])
        else:
            answer += int(value)
    return answer



print(solution("-1 -2 -3 Z"))
