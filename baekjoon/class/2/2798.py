from itertools import *

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
total = 0
comb_list = list(combinations(num_list, 3))
# 순열 조합 라이브러리 itertools 모듈의 combinations 함수 사용
sum_list = []

for i in comb_list:
    sum_list.append(sum(i))

for i in sorted(sum_list, reverse=True):
    if i <= m:
        print(i)
        break


# 파이썬으로 경우의 수 구하기
# itertools 라이브러리 활용
# from itertools import *

# 1. 순열 permutations
# 순서는 있으나 중복은 없는 경우의 수
# dataset = ['A', 'B', 'C']
# printList = list(permutations(dataset, 2))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# 2. 조합 combinations
# 순서 상관없는 경우의 수 나열
# dataset = ['A', 'B', 'C']
# printList = list(combinations(dataset, 2))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 3. 중복 순열 permutation with repetition
# 중복을 허용하는 순열
# dataset = ['A', 'B', 'C']
# printList = list(product(dataset, repeat = 2))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

# 4. 중복 포함 combination with repetition
# 중복 포함, 순서를 고려하지 않는 경우
# dataset = ['A', 'B', 'C']
# printList = list(combinations_with_replacement(dataset, 2))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]


