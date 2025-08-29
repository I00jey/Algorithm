from itertools import combinations
from collections import defaultdict
def solution(clothes):
    answer = 1
    clothes_map = {}
    for name, kind in clothes:
        # 딕셔너리에 key가 없으면 0으로 초기화하고 1을 더함
        clothes_map[kind] = clothes_map.get(kind, 0) + 1
    for kind in clothes_map:
        answer *= (clothes_map[kind] + 1)
    return answer-1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))