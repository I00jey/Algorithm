def solution(number):
    answer = 0
    for i in number:
        answer += int(i)

    # 다른 풀이
    # answer = sum(int(x) for x in number)
    return answer % 9

print(solution("123"))
print(solution("78720646226947352489"))