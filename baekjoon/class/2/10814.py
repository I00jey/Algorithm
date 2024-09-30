# 나이순 정렬

n = int(input())
members = []
for i in range(n):
    age_str, name = input().split()
    members.append([int(age_str), name])

members.sort(key=lambda x: x[0])
for age, name in members:
    print(age, name)

# 정렬 정리
# sort()
# : 원본 자체를 정렬, None 반환

# 내림차순 정렬(기본값=False)
#    .sort(reverse=True)
# 정렬 조건을 설정할 함수 넣기
#    .sort(key=함수)
# lambda 함수 사용 가능
#    .sort(key= lambda x : -x[1])
# lambda 앞에 - 를 붙이면 reverse=True와 같은 효과


# sorted()
# : 원본 변형 X, 새로운 list 반환

# 내림차순 정렬(기본값=False)
#   sorted(list, reverse=True)
# lambda 함수 사용 가능
#    sorted(list, key= lambda x : x[0])
