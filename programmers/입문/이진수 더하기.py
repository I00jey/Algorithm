# 내 풀이
def solution(bin1, bin2):
    answer = ''
    total = 0
    bin1 = list(reversed(bin1))
    bin2 = list(reversed(bin2))
    for i in range(len(bin1)):
        total += int(bin1[i])*(2**i)
    for i in range(len(bin2)):
        total += int(bin2[i])*(2**i)
    return bin(total).replace('0b', '')


# 다른 풀이
def solution(bin1, bin2):
    # 2진수 문자열을 10진수 정수로 변환
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)

    # 두 10진수 더하기
    sum_num = num1 + num2

    # 결과를 2진수 문자열로 변환 (접두사 '0b' 제거)
    answer = bin(sum_num)[2:]
    return answer


# int()
# 다양한 진수의 숫자 문자열을 10진수 정수로 변환 가능

# int(x, base=10)
# x : 변환하고자 하는 문자열
# base : 문자열이 표현하고 있는 숫자의 진수 (기본값 10, 생략 가능)



# 다양한 진수 변환 함수
# bin()
# 정수를 2진수 문자열로 변환
# '0b'로 시작하는 문자열 반환

# oct()
# 정수를 8진수 문자열로 변환
# '0o'로 시작하는 문자열 반환

# hex()
# 정수를 16진수 문자열로 변환
# '0x'로 시작하는 문자열 반환

