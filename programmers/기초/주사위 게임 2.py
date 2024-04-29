def solution(a, b, c):
    if a != b and b!= c and c != a:
        answer = a + b + c
    elif a == b and b == c and c == a:
        answer = (a+b+c)*(pow(a,2)+pow(b,2)+pow(c,2))*(pow(a,3)+pow(b,3)+pow(c,3))
    else:
        answer = (a+b+c)*(pow(a,2)+pow(b,2)+pow(c,2))
    return answer

print(solution(2, 6, 1))
print(solution(5, 3, 3))
print(solution(4, 4, 4))