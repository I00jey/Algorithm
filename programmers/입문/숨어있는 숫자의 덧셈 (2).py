def solution(my_string):
    answer = 0
    arr = [i if i.isdigit() else ' ' for i in my_string ]
    string = ''.join(arr)
    nums = string.split()
    for i in nums:
        answer += int(i)
    return answer

# 문자열에서 숫자가 아닐 경우 ' ' 공백으로 변환
# split() 함수를 통해 공백 제거
# 숫자만 남은 배열을 통해 총합 구하기


# 다른 풀이
import re
# 정규 표현식을 다루기 위한 모듈

def solution(my_string):
    return sum([int(i) for i in re.findall(r'[0-9]+', my_string)])
# re.findall()
# 주어진 정규 표현식과 매칭되는 모든 부분 문자열을 찾아 리스트로 반환
# r'[0-9]+'
# 하나 이상의 연속된 숫자를 찾음
