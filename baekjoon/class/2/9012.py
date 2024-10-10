# 괄호

# 입력 데이터 수
n = int(input())
vps = []
for i in range(n):
    test_case = input()
    for a in test_case:
        if a == '(':
            vps.append('(')
        else:
            if len(vps) == 0:
                vps.append('NO vps')
                break
            if vps[-1] == '(':
                vps.pop()

    if len(vps) == 0:
        print('YES')
    else:
        print('NO')

    vps.clear()
