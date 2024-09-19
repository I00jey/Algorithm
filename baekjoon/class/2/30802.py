size = ['S', 'M', 'L', 'XL', 'XXL', 'XXXL']
n = int(input())
shirt = list(map(int, input().split(" ")))
t, p = map(int, input().split())
shirt_count = 0
for i in shirt:
    if i % t == 0:
        shirt_count += i//t
    else:
        shirt_count += (i//t + 1)
print(shirt_count)
print(n//p, n%p)