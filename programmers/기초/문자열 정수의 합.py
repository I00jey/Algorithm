# 내 풀이
# def solution(num_str):
#     answer = 0
#     num = int(num_str)
#     while num > 0:
#         answer += num % 10
#         num = num // 10
#     return answer


# 다른 풀이
def solution(num_str):
    print(num_str) # 421
    print(map(int, num_str)) # <map object at 0x00000212E6D89E70>
    return sum(map(int, num_str)) #7

# map(함수, 순회 가능한 데이터)
# 함수가 적용된 iterator 반환
# sum(반환 iterator)
# iterator를 순회하면 총합을 구함


print(solution('421'))