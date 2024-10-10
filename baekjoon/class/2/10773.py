# 제로

# 숫자 입력 횟수
k = int(input())
# 숫자 합 변수
numbers = []
for i in range(k):
    number = int(input())
    if number == 0:
        numbers.pop()
    else:
        numbers.append(number)

print(sum(numbers))