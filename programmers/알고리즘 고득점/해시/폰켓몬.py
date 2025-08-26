# from itertools import combinations
# def solution(nums):
#     answer = 0
#     n = len(nums)//2
#     comb = combinations(nums, n)
#     lis_c = list(comb)
#     arr = []
#     for i in lis_c:
#         arr.append(len(set(i)))
#     answer = max(arr)
#     return answer

def solution(nums):
    answer = 0
    # 내가 뽑을 수 있는 포켓몬 수
    n = len(nums)//2
    # 종류의 갯수
    set_n = len(set(nums))
    answer = min(set_n, n)
    # 내가 뽑는 포켓몬 수 > 종류의 개수 = 종류 수가 최대
    # 내가 뽑는 포켓몬 수 < 종류의 개수 = 내가 뽑는 수가 최대
    return answer


print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))