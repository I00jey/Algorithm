
while True:
    try:
        a, b = map(int, input().split())
        # a, b에 int형이 들어간다면 a+b값 출력
        print(a+b)
    except:
        # try에 대한 에러가 발생한 경우, while 탈출
        break
