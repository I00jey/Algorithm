test = int(input())
for i in range(test):
    h, w, n = map(int, input().split())
    if n % h == 0:
        yy = str(h)
        xx = str(n//h)
    else:
        yy = str(n % h)
        xx = str(n//h+1)

    if len(xx) == 1:
        print(f'{yy}0{xx}')
    else:
        print(yy+xx)
