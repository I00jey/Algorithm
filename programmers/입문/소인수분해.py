# 첫번째 풀이
# def solution(n):
#     answer = []
#     moks = [i for i in range(1, n+1) if n % i == 0]
#     if n == 2:
#         answer.append(2)
#     while n > 2:
#         for i in moks:
#             if len([i for j in range(1, i+1) if i % j == 0]) == 2:
#                 n = n // i
#                 answer.append(i)
#     return sorted(answer)


# 두번째 풀이
def solution(n):
    answer = []
    i = 2
    if n == 2:
        answer.append(2)
    while i * i <= n:
        if n % i == 0:
            n = n // i
            answer.append(i)
        else:
            i += 1
    return sorted(answer)

# 세번째 풀이


print(solution(2))
print(solution(10000))
