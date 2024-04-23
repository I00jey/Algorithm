def lotto(depth, start, path):
    # depth 즉 조합이 길이가 6개가 된다면 출력 후 return
    if depth == 6:
        print(*path)
        return

    # 현재
    for i in range(start, len(lis)):
        # list[-1]은 마지막 인덱스
        # 현재 고려 중인 숫자가 이전에 선택된 숫자들에 없고, 현재까지의 조합의 마지막 숫자보다 크다면
        # 중복 검사 && 리스트 마지막 인덱스 값과 크기 비교
        if lis[i] not in path and path[-1] < lis[i]:
            path.append(lis[i])
            lotto(depth + 1, start, path)
            path.pop()



while True:
    # 입력값 빈칸을 기준으로 분할하여 리스트 저장
    inp = list(map(int, input().split(" ")))
    # 입력 첫번째 값은 집합 요소 수
    num = inp[0]
    # 입력 나머지 값은 집합 요소 리스트
    lis = inp[1:]

    # 입력값이 0이면 while문 탈출
    if num == 0:
        break

    # range(7)이면 값은 0~6
    # 만약 집합 수가 7이라면 시작 인덱스는 0, 1이 가능
    for start in range(len(lis) - 6 + 1):
        lotto(1, start, [lis[start]])
    # 테스트케이스 사이에 빈 줄 넣기
    print()
