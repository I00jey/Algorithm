# def solution(binomial):
#     return eval(binomial)

def solution(binomial):
    op = ""
    for i in binomial:
        if not i.isdigit():
            op = i
    answer = binomial.split(op)
    return eval(answer[0]+answer[1]+answer[2])


print(solution("43 + 12"))
print(solution("0 - 7777"))
print(solution("40000 * 40000"))