# 통계학

#내 풀이 (시간 초과)
# import sys
# input = sys.stdin.readline
#
# # 수의 개수 입력
# n = int(input())
#
# # 수를 저장할 리스트
# numbers = []
# # 수 입력
# for _ in range(n):
#     numbers.append(int(input()))
#
# # 산술 평균
# print(round(sum(numbers)/n))
#
# # 중앙값
# print(sorted(numbers)[n//2])
#
# # 최빈값
# count_lis = [[] for _ in range(n+1)]
# for i in numbers:
#     count_lis[numbers.count(i)].append(i)
# # 리스트.count()
# # 각 리스트에서 각 숫자의 빈도를 구할 때, 전체 리스트를 순회하기 때문에 => O(n^2)
#
# count_lis.reverse()
# # print(count_lis)
# for count in count_lis:
#     if len(count) == 1:
#         print(count[0])
#         break
#     elif len(count) > 1:
#         if len(set(count)) == 1:
#             print(count[0])
#         else:
#             print(sorted(set(count))[1])
#         break
# # print(count_lis)
#
# # 범위
# print(max(numbers)-min(numbers))


# -------------------------------------------------------------------
# 다른 풀이 (collections.Counter 사용)
# import sys
# # collections.Counter를 사용하여 각 숫자의 빈도를 미리 계산 => O(n)
# from collections import Counter
#
# input = sys.stdin.readline
#
# # 수의 개수 입력
# n = int(input())
#
# # 수를 저장할 리스트
# numbers = []
# # 수 입력
# for _ in range(n):
#     numbers.append(int(input()))
#
# # 산술 평균
# print(round(sum(numbers)/n))
#
# # 중앙값
# print(sorted(numbers)[n//2])
#
# # 최빈값 (효율적인 방식, 시간초과 X)
# count = Counter(numbers).most_common()
# # print(count)
# # 예시) [(1, 1), (3, 1), (8, 1), (-2, 1), (2, 1)] 튜플 리스트
#
# # 최빈값 리스트를 빈도 수 기준으로 내림차순 정렬
# max_freq = count[0][1]
# # print(max_freq)
#
# # 최빈값 리스트 초기화
# modes = [num for num, freq in count if freq == max_freq]
# # print(modes)
#
# # 최빈값이 여러 개일 경우 두 번째로 작은 값 출력
# if len(modes) > 1:
#     print(sorted(modes)[1])
# else:
#     print(modes[0])
#
# # 범위
# print(max(numbers)-min(numbers))

# --------------------------------------------------------------
# 다른 풀이2 (최빈값 dict 사용)
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = []
#
# for i in range(n):
#     arr.append(int(input()))
#
# # 중앙값을 구하기 위해 정렬
# arr.sort()
#
# # 1) 산술평균
# print(round(sum(arr) / len(arr)))
# # 2) 중앙값
# print(arr[len(arr) // 2])
#
# # 3) 최빈값
# dic = dict()
# for i in arr:  # 빈도수 구하기
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
#
# mx = max(dic.values())  # 빈도수 중 최대값 구하기
# mx_dic = []  # 최빈값 숫자를 저장할 배열
#
# for i in dic:  # 빈도수 딕셔너리에서
#     if mx == dic[i]:  # 최빈값의 key저장
#         mx_dic.append(i)
#
# if len(mx_dic) > 1:  # 최빈값이 여러개라면
#     print(mx_dic[1])  # 두번째로 작은 값
# else:  # 하나라면
#     print(mx_dic[0])  # 해당 값 출력
#
# print(max(arr) - min(arr))


# -----------------------------------------------
# collections 모듈의 Counter
# from collections import Counter


# Counter 생성자
# 중복된 데이터가 있는 리스트를 인자로 넘기면 각 원소의 빈도가 저장된 객체 반환
# >>> Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
# Counter({'hi': 3, 'hey': 2, 'hello': 1})
# 문자열을 인자로 넘기면 각 문자가 문자열에서 몇번씩 나타나는지 알려주는 객체 반환
# >>> Counter("hello world")
# Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})


# Counter 클래스는 dictionary 딕셔너리를 확장하고 있기 때문에 딕셔너리에서 제공하는 API 그대로 사용 가능
# counter = Counter("hello world")
# counter["o"], counter["l"]
# (2, 3)


# 딕셔너리로 Counter 구현
# def countLetters(word):
#     counter = {}
#     for letter in word:
#         if letter not in counter:
#             counter[letter] = 0
#         counter[letter] += 1
#     return counter
#
# countLetters('hello world'))


# Counter 메소드
# Counter.most_common()
# 데이터의 개수가 많은 순으로 정렬된 배열을 리턴
# Counter('hello world').most_common()
# [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]

# 인자로 숫자 K를 넘기면 그 숫자 만큼만 리턴하기 때문에, 가장 개수가 많은 K개의 데이터




# 산술 연산자 활용
# 숫자처럼 산술 연산자를 사용가능
# counter1 = Counter(["A", "A", "B"])
# counter2 = Counter(["A", "B", "B"])
# 더하기
# counter1 + counter2
# Counter({'A': 3, 'B': 3})
# 빼기
# counter1 - counter2
# Counter({'A': 1})
# 🚨뺄샘의 결과로 0이나 음수가 나온 경우에는 최종 카운터 객체에서 제외