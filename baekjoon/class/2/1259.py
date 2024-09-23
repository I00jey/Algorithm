while True:
    number = input()
    if number == '0':
        break
    # 주어진 수의 길이가 홀수일 경우
    if len(number) % 2 == 1:
        a = number[:len(number)//2]
        # 가운데 숫자 포함 X
        b = number[(len(number)+1)//2:]
        # 가운데 숫자를 포함하지 않기때문에 + 1
        if a == b[::-1]:
            print('yes')
        else:
            print('no')
    # 주어진 수의 길이가 짝수일 경우
    else:
        # 주어진 수를 반으로 나누기
        a = number[:len(number)//2]
        b = number[len(number)//2:]
        if a == b[::-1]:
            print('yes')
        else:
            print('no')

# 다른 풀이
# 입력값을 반으로 나눠서 비교하지않고, 입력값 자체를 뒤집어서 비교
while True:
    n = input()

    if n == '0':
        break

    if n == n[::-1]:
        print('yes')
    else:
        print('no')