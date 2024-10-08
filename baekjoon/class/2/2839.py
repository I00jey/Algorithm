# 설탕 배달

# 설탕 총량 입력
n = int(input())
# 사용한 봉지 수 리스트
result = []
# 사용한 봉지 수
count = 0

# sugar 가변
# n 불변
sugar = n

# 최대 경우의 수
# 5보다 3으로 나누었을 때 최대
a = n // 3
# 3키로의 봉투가 0 - a개일 때의 경우
for i in range(a+1):
    # 전체 무게에서 3키로 봉투 무게 제외
    sugar = sugar - 3 * i
    # 3키로 봉투를 제외한 무게가 5로 나누어 떨어지면
    if sugar % 5 == 0:
        # 3키로 봉투 개수 추가
        count += i
        # 5키로 봉투 개수 추가
        count += sugar // 5
        # 봉투 개수 리스트에 추가
        result.append(count)

    # 봉투 개수 초기화
    count = 0
    # 총 설탕 무게 초기화
    sugar = n

# print(result)

# 3키로와 5키로 봉투로 정확히 나눌 수 없다면
if len(result) < 1:
    print(-1)
else:
    # 구한 경우의 수 중 최소 봉투 개수
    print(min(result))



# ---------------------------------------------------
# 다른 풀이
# while 사용
# 설탕 총량 입력
n = int(input())

# 사용한 봉지 수
count = 0

while n >= 0:
    # 5kg 봉지로 나눠 떨어지면 5kg 봉지를 최대한 사용
    if n % 5 == 0:
        count += n // 5
        print(count)
        break
    # 5kg 봉지로 나눠 떨어지지 않으면 3kg 봉지를 사용
    n -= 3
    count += 1
    # 설탕 무게가 5로 나누어 떨어지지 않는다면
    # 설탕 무게를 3씩 빼고 (3키로 봉투를 하나 사용하고) 봉투 개수 +1

else:
    # 정확히 나눌 수 없으면 -1 출력
    print(-1)