# 풀이 1
# 시간초과
# n = int(input())
# n_lis = list(input().split())
#
# m = int(input())
# m_lis = list(input().split())
#
# for i in m_lis:
#     if i in n_lis:
#         print(1)
#     else:
#         print(0)

# ------------------------------------
# 풀이 2
# readline() 사용
# 시간 초과
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# n_lis = input().split()
#
# m = int(input())
# m_lis = input().split()
#
# for i in m_lis:
#     if i != ' ':
#         if i in n_lis:
#             print(1)
#         else:
#             print(0)


# ---------------------------
# 풀이 3
# sys.stdin.readline() 사용
# 기준이 되는 N개의 정수를 set()함수로 집합으로 변환
# 집합은 내부적으로 테이블을 사용하기 때문에 조회시간이 매우 빠름

import sys
n = int(sys.stdin.readline())
n_lis = set(sys.stdin.readline().split())

m = int(sys.stdin.readline())
m_lis = sys.stdin.readline().split()

for i in m_lis:
    if i in n_lis:
        print(1)
    else:
        print(0)