# 나는야 포켓몬 마스터 이다솜

import sys

n, m = map(int, sys.stdin.readline().split())

# 번호로 포켓몬(이름)을 찾기위한 리스트
pocket_mon = [0 for _ in range(n+1)]

# 이름으로 포켓폰(번호)를 찾기위한 딕셔너리
# 딕셔너리에서의 탐색 => 평균 O(1)
pocket_mon_dict = {}

# 포켓몬 정보 입력받기
for i in range(1, n+1):
    name = sys.stdin.readline().strip()
    # 리스트에 이름 저장
    pocket_mon[i] = name
    # 딕셔너리에 이름:번호 형태로 저장
    pocket_mon_dict[name] = i
    # 포켓몬 이름으로 번호를 빠르게 탐색하기 위해


for _ in range(m):
    question = sys.stdin.readline().strip()
    if question.isdigit():
        print(pocket_mon[int(question)])
    else:
        print(pocket_mon_dict[question])
        # print(pocket_mon.index(question))
        # 시간초과 발생
        # 리스트의 인덱스를 찾는 연산은 비효율적 => O(n) 모든 요소 탐색

# input() vs sys.stdin.readline()
# input()
# : 입력을 받을 때, 자동으로 개행 문자(\n) 제거
# sys.stdin.readline()
# : 입력된 문자열 끝에 개행 문자(\n) 포함한 채로 값 반환
# => strip(), rstrip() 사용해서 개행문자 수동 제거