numbers = list(map(int, input().split()))
if sorted(numbers) == numbers:
    print('ascending')
elif sorted(numbers, reverse=True) == numbers:
    print('descending')
else:
    print('mixed')
