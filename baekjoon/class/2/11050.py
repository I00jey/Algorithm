# 재귀 함수 사용
# 런타임에러 RecursionError
# 파이썬이 정한 최대 재귀 깊이를 재귀의 깊이가 초과했을 때 발생
# def fun(num):
#     if num == 1:
#         return 1
#     return num * fun(num-1)
#
#
# n, k = map(int, input().split())
# print(fun(n)//(fun(k)*fun(n-k)))


# for문 사용
n, k = map(int, input().split())
output = 1
for num in range(1, n+1):
    output *= num

for num in range(1, k+1):
    output /= num

for num in range(1, (n-k)+1):
    output /= num

print(output)



# 개념
# 이항계수
# 이항식을 이항정리로 전개했을 때 각 항의 계수를 나타냄
# (x+y) * (x+y) = x*x + 2xy + y*y
# 각항의 계수인 [1, 2, 1] => 이항계수

# 점화식 성립
# 0 <= k <= n
# 이항계수 == n! // k! * (n-k)!