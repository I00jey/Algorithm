# 소수 구하기

# 내 풀이 (시간 초과)
# import sys
# m, n = map(int, sys.stdin.readline().split())
# yak_su = []
# numbers = [i for i in range(m, n+1)]
#
# for i in range(m, n+1):
#     for j in range(2, int(n**0.5)+1):
#         if i % j == 0:
#             yak_su.append(i)
#
# so_su = [i for i in numbers if i not in yak_su]
# # print(set(yak_su))
# # print(so_su)
#
# for i in so_su:
#     print(i)



# 에라토스테네스의 체 풀이
import sys
import math

m, n = map(int, sys.stdin.readline().split())
# 0부터 n까지 소수여부를 저장할 리스트
is_prime = [True] * (n+1)
# 0과 1은 소수가 아님
is_prime[0] = is_prime[1] = False

# 2에서 범위 최댓값의 제곱근(정수)까지
for i in range(2, int(math.sqrt(n)) + 1):
    # 소수가 맞다면
    if is_prime[i]:
        # i*i부터 i의 배수 제거
        for j in range(i*i, n+1, i):
            is_prime[j] = False

# 범위내 소수만 출력
for i in range(m, n+1):
    if is_prime[i]:
        print(i)

# 에라토스테네스의 체 원리
# 1. 소수 판별
# 2. 배수 제거 (판별한 소수들의 배수를 제거)

# i*i부터 범위가 시작하는 이유
# => i의 이전 배수들은 이미 처리됨
# => i의 배수 중에서 처음 처리되지 않은 배수는 i * i