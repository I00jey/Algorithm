def solution(strArr):
    return [str.lower() if idx % 2 == 0 else str.upper() for idx, str in enumerate(strArr)]


print(solution(["AAA","BBB","CCC","DDD"]))
print(solution(["aBc","AbC"]))