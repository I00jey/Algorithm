testcase = int(input())
for i in range(testcase):
    string = input()
    lis = string.split('X')
    point = 0
    score = 0
    for x in lis:
        for y in range(1, len(x)+1):
            point += y
        score += point
        point = 0

    print(score)


