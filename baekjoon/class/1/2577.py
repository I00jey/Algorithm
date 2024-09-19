a = int(input())
b = int(input())
c = int(input())
number = a * b * c
dic = dict.fromkeys('0123456789', 0)
for i in str(number):
    dic[i] += 1

for i in dic.values():
    print(i)
