
input_list = []
for _ in range(3):
    input_list.append(input())

for idx, value in enumerate(input_list):
    if value.isdigit():
        output = int(value) + (3 - idx)


if output % 3 == 0 and output % 5 == 0:
    print('FizzBuzz')
elif output % 3 == 0 and output % 5 != 0:
    print('Fizz')
elif output % 3 != 0 and output % 5 == 0:
    print('Buzz')
else:
    print(output)

