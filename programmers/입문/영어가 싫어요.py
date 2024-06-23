# 내 풀이
def solution(numbers):
    # 딕셔너리에 문자열에 따른 숫자 문자 저장
    dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    for key, value in dic.items():
        if key in numbers:
            print(key, value)
            numbers = numbers.replace(key, value)
    return int(numbers)


print(solution("onetwothreefourfivesixseveneightnine"))

# 다른 풀이
def solution(numbers):
    # 리스트 활용
    # 숫자 데이터 저장없이 인덱스 활용
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)