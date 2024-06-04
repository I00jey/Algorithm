def solution(myString, pat):
    arr = [myString[i:i+len(pat)] for i in range(len(myString))]
    return arr.count(pat)


print(solution("banana", "ana"))
print(solution("aaaa", "aa"))