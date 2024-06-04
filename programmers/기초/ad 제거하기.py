# 내 풀이
# 테스트 케이스 2개 맞고 다 틀림
# for str in strArr[:] 과 for str in strArr의 차이를 모르겠음
def solution(strArr):
    for str in strArr[:]:
        if 'ad' in str:
            strArr.remove(str)
    return strArr


# 다른 풀이
def solution(strArr):
    return [i for i in strArr if 'ad' not in i]


print(solution(["and","notad","abcd"]))
print(solution(["there","are","no","a","ds"]))