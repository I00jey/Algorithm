# ATM

# 사람 수 입력받기
n = int(input())
# 각 사람의 인출 시간
p = list(map(int, input().split()))

# 인출 시간을 오름차순으로 정렬
p.sort()

# 총 인출 시간의 합
total_time = 0
# 현재 인출 시간의 합
current_time = 0

for time in p:
    current_time += time
    total_time += current_time

# 출력
print(total_time)
