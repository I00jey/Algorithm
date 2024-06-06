def solution(myString):
    answer = [i for i in myString.split("x") if i]
    answer.sort()
    return answer

# for문 내에서 "" 빈 값을 제거하면 인덱스가 바뀌어 테스트 케이스 실패!
# 직접적으로 빈값 요소 하나하나를 삭제하기보다는 filter 함수나 if-for문을 이용해서 풀기

print(solution("axbxcxdx"))
print(solution("dxccxbbbxaaaa"))
print(solution("xcxxaxxbx"))