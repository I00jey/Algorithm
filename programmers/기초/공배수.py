def solution(number, n, m):
    return int(number%n==0 and number%m==0)

print(solution(60,2,3))
print(solution(55,10,5))