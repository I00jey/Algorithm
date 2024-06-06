def solution(myString):
    answer = myString.split("x")
    return [len(i) for i in answer]


print(solution("oxooxoxxox"))
print(solution("xabcxdefxghi"))