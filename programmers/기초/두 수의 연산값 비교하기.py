def solution(a, b):
    oper = int(f'{a}{b}')
    return max(oper, 2*a*b)

print(solution(2, 91))
print(solution(91, 2))