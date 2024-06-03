def solution(myString, pat):
    return 1 if pat.upper() in myString.upper() else 0


print(solution("AbCdEfG", "aBc"))
print(solution("aaAA", "aaaaa"))