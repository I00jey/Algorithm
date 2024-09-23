r = 31
m = 1234567891


# 문자열의 길이
n = int(input())
# 문자열 입력
string = input()
# 알파벳 소문자 리스트 만들기
alpha_list = [chr(i) for i in range(97, 97+26)]
# 문자열에 따른 수열
int_list = [alpha_list.index(i)+1 for i in string]
# 해싱함수 결과
output = [value*pow(r, idx) for idx, value in enumerate(int_list)]
# 해싱함수 결과의 합을 m으로 나눈 나머지
print(sum(output) % m)