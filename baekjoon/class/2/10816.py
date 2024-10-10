# 숫자 카드 2

n = int(input())
cards = list(map(int, input().split()))

dic = dict.fromkeys(cards, 0)

for i in cards:
    dic[i] += 1


m = int(input())
numbers = list(map(int, input().split()))
output = []
for i in numbers:
    if i in dic.keys():
        output.append(dic[i])
    else:
        output.append(0)

for i in output:
    print(i, end=' ')