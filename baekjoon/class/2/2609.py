# 다른 풀이
# 유클리드 호제법 사용
a, b = map(int, input().split())
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

yak = gcd(a, b)
print(yak)
# 최대공배수는 두수의 곱을 최대공약수로 나눈 값
print(a * b // yak)

# 다른 풀이 2
# math 모듈 속 최대공약수 & 최소공배수 함수 사용
import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))


# 내 풀이 (정답 X, 공약수를 찾는 과정에서 일부 경우 누락가능)
a, b = map(int, input().split())
a_list = [i for i in range(2, a + 1) if a % i == 0]
b_list = [i for i in range(2, b + 1) if b % i == 0]
ab_list = []

for i in a_list:
    if i in b_list:
        ab_list.append(i)

if ab_list:
    yak = max(ab_list)
    print(yak)
    print(a // yak * b // yak * yak)



# 유클리드 호제법
# 호제법 : 두 수가 서로 상대방의 수를 나누어서 결국 원하는 수를 얻는 알고리즘
# 2개의 자연수 a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a > b),
# a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
# 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수
