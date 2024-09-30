# 666이 포함된 수를 저장할 리스트
movie_list = []
# 최소값 666 시작
i = 665
n = int(input())

while True:
    i += 1
    if '666' in str(i):
        movie_list.append(i)
    if len(movie_list) == n:
        break

# 리스트 중 가장 큰 수 출력
print(movie_list[-1])

