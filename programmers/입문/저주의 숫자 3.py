def solution(n):
    now = 0
    # 마을에서 사용하는 숫자로의 변환을 n번 진행
    for i in range(n):
        # 기존 수에서 +1
        now += 1
        # 1 더한 수가 3의 배수이거나 숫자 '3'을 포함하면 +1
        while now % 3 == 0 or '3' in str(now):
            now += 1
    return now


print(solution(10))