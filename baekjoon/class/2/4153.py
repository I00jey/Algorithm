while True:
    arr = sorted(list(map(int, input().split())))
    if 0 in arr:
        break
    else:
        if arr[2]**2 == arr[0]**2 + arr[1]**2:
            print('right')
        else:
            print('wrong')
