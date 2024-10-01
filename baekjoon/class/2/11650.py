# 좌표 정렬하기

n = int(input())
dots = []
for _ in range(n):
    x, y = map(int, input().split())
    dots.append((x, y))

dots.sort(key=lambda x: (x[0], x[1]))

for x, y in dots:
    print(x, y)