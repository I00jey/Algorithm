def solution(x1, x2, x3, x4):
    answer = (x1 or x2) and (x3 or x4)
    # answer = (x1 | x2) & (x3 | x4)
    return answer


print(solution(False,True,True,True))
print(solution(True,False,False,False))