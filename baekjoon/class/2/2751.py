# 수 정렬하기 2
import sys
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))


numbers.sort()
for i in numbers:
    print(i)

# 기존 문제와 같이 for문 안에 input으로 입력받았더니 <시간초과>
# 입력받는 수의 개수가 N(1 ≤ N ≤ 1,000,000)이므로 시간이 오래 걸림

# input이 sys.stdin.readlind()보다 느린이유
# => input 함수는 prompt message를 출력하고, 개행문제를 삭제한 값을 리턴하기 때문
# => sys.stdin.readline()은 prompt message를 인수로 받지 않음 & 개행 문자를 포함한 값을 리턴