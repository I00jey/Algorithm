# 좌표 정렬하기 2

n = int(input())
dots = []

for _ in range(n):
    x, y = map(int, input().split())
    dots.append((x, y))

dots.sort(key=lambda a: (a[1], a[0]))

for x, y in dots:
    print(x, y)