# 배수 제외한 배열 크기
# n = int(input())
# arr = list(map(int, input().split()))
# output = []
# for i in arr:
#     if i == 1:
#         continue
#     elif i > 2 and i % 2 == 0:
#         continue
#     elif i > 3 and i % 3 == 0:
#         continue
#     elif i > 5 and i % 5 == 0:
#         continue
#     elif i > 7 and i % 7 == 0:
#         continue
#     else:
#         output.append(i)
#
# print(len(output))

#--------------------------------------

# 에라토스테네스의 체
n = int(input())
arr = list(map(int, input().split()))
# 소수 개수를 저장할 변수
sosu = 0

# 주어진 숫자 배열 반복
for element in arr:
    # 1은 소수가 아님
    if element == 1:
        continue
    # 주어진 수의 제곱근까지로 범위 좁힘
    # 제곱근까지의 수 중 나누어 떨어지는 수가 있다면 반복 중단
    for i in range(2, int(element**(1/2))+1):
        if element % i == 0:
            break
    # 제곱근까지의 수 중 나누어 떨어지는 수가 없다면 소수 개수 1 증가
    else:
        sosu += 1

print(sosu)
