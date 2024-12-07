# 패션왕 신해빈

# 테스트 케이스 수 입력
t = int(input())

for i in range(t):
    # 입력할 옷 개수 입력
    n = int(input())
    # 옷장 초기화
    clothes = {}
    # 옷 종류, 이름 입력
    for j in range(n):
        name, kind = input().split()
        if kind in clothes.keys():
            clothes[kind].append(name)
        else:
            clothes[kind] = [name]

    # 입력된 옷 종류, 이름 확인
    # print(clothes)

    # 경우의 수를 곱해야하므로 조합 변수 1로 초기화
    result = 1
    # 옷의 종류만큼 반복
    for kind in clothes.keys():
        # 옷의 종류별 갯수 + 1
        # +1을 하는 이유 => 해당 종류의 옷을 선택하지 않는 경우 고려 (입지않는 경우)
        result *= len(clothes[kind]) + 1

    # -1을 하는 이유 => 해빈이가 알몸이 아닌 경우를 제외해야 함
    print(result-1)

