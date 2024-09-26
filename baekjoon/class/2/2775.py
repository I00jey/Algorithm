test_case = int(input())
for _ in range(test_case):
    k = int(input())
    n = int(input())
    # 리스트 초기화
    apart = [[0 for _ in range(n)] for _ in range(k+1)]
    # 0층부터 시작
    for i in range(k+1):
        # 0층에서 n호에는 n명
        if i == 0:
            # 호는 1부터 n까지
            apart[i] = [j for j in range(1, n+1)]
        else:
            # 호는 1부터 시작하나 인덱스는 그대로 0부터 시작
            for j in range(n):
                if j == 0:
                    # 매층 1호는 1명
                    apart[i][j] = 1
                else:
                    # k층의 n호에 사는 사람 수
                    # k-1층의 n호까지의 사람 수 합
                    apart[i][j] = sum(apart[i-1][y] for y in range(j+1))
    print(apart[k][n-1])

