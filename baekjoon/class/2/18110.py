# solved.ac

# 내 풀이 (오답)
import sys

n = int(sys.stdin.readline())
numbers = []

for i in range(n):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()
none_avg = round(n * 0.15)
# print('평균계산에서 제외할 사람 수', none_avg)

numbers_jeolsa = numbers[none_avg+1: len(numbers)-none_avg]

# / 나누기 연산할 때는, 항상 ZeroDivisionError 주의
if len(numbers_jeolsa) > 0:
    avg = round(sum(numbers_jeolsa)/len(numbers_jeolsa))
    print(avg)
else:
    print(0)


# -----------------------------------------------------------
# 정답 풀이
import sys

# 직접 구현한 반올림 함수
# round()는 오사오입
def my_round(num):
    # 숫자가 5이상
    if num - int(num) >= 0.5:
        # 반올림
        return int(num)+1
    else:
        # 숫자가 4이하 => 반내림
        return int(num)


n = int(sys.stdin.readline().strip())

# 의견이 있을 때
if n:
    # 난이도 저장 리스트
    level = []
    for _ in range(n):
        level.append(int(sys.stdin.readline().strip()))

    # 난이도 의견 앞, 뒤에서 제외할 의견 수 구하기
    nn = my_round(n*0.15)
    # 난이도 오름차순 정렬
    level.sort()

    # 제외할 의견이 1 이상이면
    if nn > 0:
        print(my_round(sum(level[nn:-nn])/len(level[nn:-nn])))
    else:
        # 제외할 의견이 없다면 일반 평균 구하기
        print(my_round(sum(level)/len(level)))

# 난이도 의견이 없다면
else:
    print(0)


# 일반 반올림
# 사사오입
# 4 이하면 내림, 5 이상이면 올림

# vs

# 파이썬의 round()
# 오사오입
# 5 미만 내림, 5 초과 올림
# 5일때는 5 앞자리가 홀수인 경우 올림, 짝수인 경우 내림