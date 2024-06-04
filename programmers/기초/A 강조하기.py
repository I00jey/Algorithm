# 내 풀이
# def solution(myString):
#     myString = list(myString)
#     for idx, str in enumerate(myString):
#         if str =='a':
#             myString[idx] = 'A'
#         elif str != 'A' and str.isupper():
#             myString[idx] = str.lower()
#     return ''.join(myString)


# 다른 풀이
def solution(myString):
    return myString.lower().replace('a', 'A')


print(solution("abstract algebra"))
print(solution("PrOgRaMmErS"))