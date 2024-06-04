# 내 풀이
# def solution(myString, pat):
#     arr = reversed([myString[:i] for i in range(1, len(myString)+1)])
#     for i in arr:
#         if i.endswith(pat):
#             return i

# 다른 풀이
def solution(myString, pat):
    return myString[:myString.rindex(pat)+len(pat)]
# 지정 문자열 str이 뒤에서부터 찾아 문자열 시작 인덱스를 구하기
# 지정 문자열 길이 더하기
# 지정 문자열까지 포함되어 반환되는 슬라이싱

# rindex(str, [start], [end])
# str가 마지막으로 검색된 위치를 반환하는 함수
# 지정 문자열 없으면, ValueError: substring not found 발생.


print(solution("AbCdEFG", "dE"))
print(solution("AAAAaaaa", "a"))