si, boon = map(int, input().split())
total = si*60 + boon - 45
if total >= 0:
    print(f'{total//60} {total%60}')
else:
    total2 = 24*60 + total
    print(f'{total2//60} {total2%60}')