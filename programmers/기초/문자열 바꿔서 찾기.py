def solution(myString, pat):
    arr = ['A' if i == 'B' else 'B' for i in myString]
    str = ''.join(arr)
    return int(pat in str)


print(solution("ABBAA", "AABB"))
print(solution("ABAB", "ABAB"))

# 문자열 내에 부분 문자열이 포함되어 있는지 확인하는 방법
# 1. in
# : if 부분 in 문자열
# True / False 반환

# 2. find()
# 문자열.find(부분)
# 부분 문자열의 인덱스 / -1

# 3. index()
# 부분 문자열의 인덱스 / ValueError 발생