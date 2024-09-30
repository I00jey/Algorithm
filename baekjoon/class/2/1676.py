# 팩토리얼 0의 개수

# 풀이 1
# 재귀함수 활용
# RecursionError 발생
# => python이 정한 재귀 깊이보다 재귀의 깊이가 깊어져서

# sys.setrecursionlimit()을 사용
#  => python이 정한 최대 재귀 높이를 변경
# 단, 재귀의 깊이가 채점 서버가 감당할 수 없는 정도로 깊어지면, Segmentation fault 발생
import sys
sys.setrecursionlimit(10**6)

n = int(input())

def func(num):
    if num == 1:
        return 1
    else:
        return num * func(num-1)


output = func(n)
count = 0
for i in reversed(str(output)):
    if i == '0':
        count += 1
    else:
        print(count)
        break


# 풀이 2
# for문 사용

n = int(input())

def func(num):
    output = 1
    for i in range(1, num+1):
        output *= i
    return output


result = func(n)
count = 0
for i in reversed(str(result)):
    if i == '0':
        count += 1
    else:
        print(count)
        break

