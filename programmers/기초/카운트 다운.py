# def solution(start, end_num):
#     answer = [i for i in range(end_num, start+1)]
#     answer.reverse()
#     return answer

# 다른 풀이
def solution(start, end_num):
    return list(range(start, end_num-1, -1))

print(solution(10, 3))
print(solution(3, 0))