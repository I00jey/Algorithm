def solution(strArr):
    dic = {}
    for i in strArr:
        length = str(len(i))
        if length not in dic:
            dic[length] = 1
        else:
            dic[length] += 1
    return max(dic.values())
# 딕셔너리는 키 중복불가
# for문을 통해 문자열 배열 요소의 길이를 키값으로 딕셔너리에 저장
# 딕셔너리.values()를 통해 값들 중 가장 큰 값 출력



# 다른 풀이
def solution(strArr):
    a=[0]*31
    for x in strArr:
        a[len(x)] += 1
    return max(a)
# strArr에 저장된 원소의 길이가 30이므로 미리 배열을 0으로 초기화 시킨후
# for 문을 통해 값 저장


print(solution(["a","bc","d","efg","hi"]))
